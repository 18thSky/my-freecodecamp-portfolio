from fastapi.testclient import TestClient

from app import app
from database import get_connection


client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "status": "QA Bug API is running"
    }


def test_get_bugs():
    response = client.get("/bugs")

    assert response.status_code == 200

    data = response.json()

    assert "bugs" in data
    assert isinstance(data["bugs"], list)
    assert len(data["bugs"]) >= 45


def test_create_valid_bug():
    title = "Automated MySQL integration test bug"

    response = client.post(
        "/bugs",
        json={
            "title": title,
            "severity": "Low",
            "status": "Bugged",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == title
    assert data["severity"] == "Low"
    assert data["status"] == "Bugged"
    assert isinstance(data["id"], int)

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM bugs WHERE id = %s",
            (data["id"],),
        )
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def test_invalid_severity():
    response = client.post(
        "/bugs",
        json={
            "title": "Invalid severity test",
            "severity": "P7",
            "status": "Bugged",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid severity"


def test_invalid_status():
    response = client.post(
        "/bugs",
        json={
            "title": "Invalid status test",
            "severity": "Low",
            "status": "Open",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid status"


def test_missing_title():
    response = client.post(
        "/bugs",
        json={
            "severity": "Low",
            "status": "Bugged",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Title is required"


def test_empty_title():
    response = client.post(
        "/bugs",
        json={
            "title": "   ",
            "severity": "Low",
            "status": "Bugged",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Title is required"


def test_summary():
    response = client.get("/bugs/summary")

    assert response.status_code == 200

    summary = response.json()

    assert summary == {
        "High": 5,
        "Low": 9,
        "Medium": 16,
    }

    assert all(
        isinstance(count, int)
        for count in summary.values()
    )

def test_summary_excludes_closed_status():
    connection = get_connection()
    cursor = connection.cursor()
    test_id = None

    try:
        cursor.execute(
            """
            SELECT COALESCE(MAX(id), 0) + 1 AS test_id
            FROM bugs
            """
        )

        test_id = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO bugs (
                id,
                title,
                severity,
                status
            )
            VALUES (%s, %s, %s, %s)
            """,
            (
                test_id,
                "Closed status summary test",
                "Urgent",
                "Bug fixed",
            ),
        )

        connection.commit()

        response = client.get("/bugs/summary")

        assert response.status_code == 200

        summary = response.json()

        assert "Urgent" not in summary

    finally:
        if test_id is not None:
            cursor.execute(
                "DELETE FROM bugs WHERE id = %s",
                (test_id,),
            )
            connection.commit()

        cursor.close()
        connection.close()

def test_summary_empty_result(monkeypatch):
    class FakeCursor:
        def execute(self, query):
            pass

        def fetchall(self):
            return []

        def close(self):
            pass

    class FakeConnection:
        def cursor(self, dictionary=True):
            return FakeCursor()

        def close(self):
            pass

    def fake_get_connection():
        return FakeConnection()

    monkeypatch.setattr(
        "app.get_connection",
        fake_get_connection,
    )

    response = client.get("/bugs/summary")

    assert response.status_code == 200
    assert response.json() == {}
