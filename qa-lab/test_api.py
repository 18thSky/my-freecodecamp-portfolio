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

    assert isinstance(summary, dict)

    assert "High" in summary
    assert "Low" in summary
    assert "Medium" in summary

    assert summary["High"] == 5
    assert summary["Low"] >= 8
    assert summary["Medium"] == 16
