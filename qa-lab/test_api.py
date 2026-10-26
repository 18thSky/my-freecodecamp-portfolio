import pytest
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
    created_id = None

    try:
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
        created_id = data.get("id")

        assert data["title"] == title
        assert data["severity"] == "Low"
        assert data["status"] == "Bugged"
        assert isinstance(created_id, int)

    finally:
        if created_id is not None:
            connection = get_connection()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    "DELETE FROM bugs WHERE id = %s",
                    (created_id,),
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


def test_post_bugs_rejects_malformed_json():
    response = client.post(
        "/bugs",
        content='{"title":',
        headers={"content-type": "application/json"},
    )

    assert response.status_code == 422

    detail = response.json()["detail"]
    assert isinstance(detail, list)
    assert detail[0]["type"] == "json_invalid"
    assert detail[0]["loc"][0] == "body"


@pytest.mark.parametrize(
    "body",
    [
        pytest.param([], id="json-array"),
        pytest.param("hello", id="json-string"),
        pytest.param(None, id="json-null"),
    ],
)
def test_post_bugs_rejects_non_object_json(body):
    response = client.post("/bugs", json=body)

    assert response.status_code == 422

    detail = response.json()["detail"]
    assert isinstance(detail, list)
    assert len(detail) >= 1
    assert detail[0]["loc"][0] == "body"


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


def test_summary_excludes_closed_status(monkeypatch):
    class FakeCursor:
        def __init__(self):
            self.query = ""

        def execute(self, query, params=None):
            self.query = query

        def fetchall(self):
            return [{"severity": "High", "count": 2}]

        def close(self):
            pass

    class FakeConnection:
        def __init__(self):
            self.fake_cursor = FakeCursor()

        def cursor(self, dictionary=False):
            return self.fake_cursor

        def close(self):
            pass

    fake_connection = FakeConnection()

    monkeypatch.setattr(
        "app.get_connection",
        lambda: fake_connection,
    )

    response = client.get("/bugs/summary")

    assert response.status_code == 200
    assert response.json() == {"High": 2}

    query = " ".join(fake_connection.fake_cursor.query.split())

    expected_open_statuses = [
        "Bugged",
        "Existing Bug",
        "Non-Recreatable",
        "QC Change",
        "New Req",
    ]

    assert "WHERE status IN" in query

    for status in expected_open_statuses:
        assert f"'{status}'" in query

    assert "'Bug fixed'" not in query
    assert "'Bug verified'" not in query


def test_summary_empty_result(monkeypatch):
    class FakeCursor:
        def execute(self, query, params=None):
            self.query = query

        def fetchall(self):
            return []

        def close(self):
            pass

    class FakeConnection:
        def cursor(self, dictionary=False):
            return FakeCursor()

        def close(self):
            pass

    monkeypatch.setattr(
        "app.get_connection",
        lambda: FakeConnection(),
    )

    response = client.get("/bugs/summary")

    assert response.status_code == 200
    assert response.json() == {}


def test_summary_controlled_aggregation(monkeypatch):
    controlled_bugs = [
        {"severity": "High", "status": "Bugged"},
        {"severity": "Low", "status": "Existing Bug"},
        {"severity": "High", "status": "Bug fixed"},
    ]

    open_statuses = {
        "Bugged",
        "Existing Bug",
        "Non-Recreatable",
        "QC Change",
        "New Req",
    }

    class FakeCursor:
        def __init__(self):
            self.query = ""

        def execute(self, query, params=None):
            self.query = query

        def fetchall(self):
            normalized_query = " ".join(self.query.split())

            assert "WHERE status IN" in normalized_query

            for status in open_statuses:
                assert f"'{status}'" in normalized_query

            counts = {}

            for bug in controlled_bugs:
                if bug["status"] in open_statuses:
                    severity = bug["severity"]
                    counts[severity] = counts.get(severity, 0) + 1

            return [
                {"severity": severity, "count": count}
                for severity, count in sorted(counts.items())
            ]

        def close(self):
            pass

    class FakeConnection:
        def cursor(self, dictionary=False):
            return FakeCursor()

        def close(self):
            pass

    monkeypatch.setattr(
        "app.get_connection",
        lambda: FakeConnection(),
    )

    response = client.get("/bugs/summary")

    assert response.status_code == 200
    assert response.json() == {
        "High": 1,
        "Low": 1,
    }
