from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "QA Bug API is running"


def test_create_valid_bug():
    response = client.post(
        "/bugs",
        json={
            "title": "Automated test bug",
            "severity": "P2",
            "status": "Open",
        },
    )

    assert response.status_code == 201


def test_invalid_severity():
    response = client.post(
        "/bugs",
        json={
            "title": "Invalid severity",
            "severity": "P7",
            "status": "Open",
        },
    )

    assert response.status_code == 400


def test_missing_title():
    response = client.post(
        "/bugs",
        json={
            "severity": "P1",
            "status": "Open",
        },
    )

    assert response.status_code == 400


def test_summary():
    response = client.get("/bugs/summary")

    assert response.status_code == 200

    summary = response.json()

    assert "P0" in summary
    assert "P1" in summary
    assert summary["P0"] >= 0
    assert summary["P1"] >= 0