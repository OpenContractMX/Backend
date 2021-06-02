from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_should_get_contacts():

    response = client.get("/api/contracts?category=social&year=2016")
    assert response.status_code == 200


def test_should_not_get_contacts_because_month_and_trimester():

    response = client.get(
        "/api/contracts?category=social&year=2016&month=0&trimester=0"
    )
    assert response.status_code == 400


def test_should_not_get_contacts_because_category():

    response = client.get("/api/contracts?category=mal&year=2016")
    assert response.status_code == 400


def test_should_not_get_contacts_because_year():

    response = client.get("/api/contracts?category=social&year=2122")
    assert response.status_code == 400


def test_should_not_get_contacts_because_month():

    response = client.get("/api/contracts?category=social&year=2016&month=123")
    assert response.status_code == 400


def test_should_not_get_contacts_because_trimester():

    response = client.get("/api/contracts?category=social&year=2016&trimester=123")
    assert response.status_code == 400
