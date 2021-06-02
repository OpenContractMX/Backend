from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_should_get_contracts_csv_by_year():

    response = client.get("/api/download?category=social&year=2016")
    assert response.status_code == 200


def test_should_get_contracts_csv_by_month():

    response = client.get("/api/download?category=social&year=2015&month=6")
    assert response.status_code == 200


def test_should_get_contracts_csv_by_trimester():

    response = client.get("/api/download?category=social&year=2015&trimester=3")
    assert response.status_code == 200


def test_should_not_get_contracts_csv_by_year():

    response = client.get("/api/download?category=social&year=2020")
    assert response.status_code == 400


def test_should_not_get_contracts_csv_by_month():

    response = client.get("/api/download?category=social&month=13")
    assert response.status_code == 400


def test_should_not_get_contracts_csv_by_trimester():

    response = client.get("/api/download?category=social&trimester=5")
    assert response.status_code == 400


def test_should_not_get_contracts_csv_by_year_because_month_and_trimester():

    response = client.get(
        "/api/download?category=social&year=2016&month=5&trimester=20"
    )
    assert response.status_code == 400


def test_should_not_get_contracts_csv_by_month_because_trimester():

    response = client.get("/api/download?category=social&month=6&year=2015&trimester=3")
    assert response.status_code == 400


def test_should_not_get_contracts_csv_by_trimester_because_month():

    response = client.get("/api/download?category=social&trimester=3&year=2015&month=6")
    assert response.status_code == 400
