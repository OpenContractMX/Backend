from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_contracts():
    
    response = client.get(
        "/api/contracts?category=social&year=2016&month=0&trimester=0"
    )
    assert response.status_code == 200

    response = client.get(
        "/api/contracts?category=social&year=2016&month=0&trimester=0"
    )
    assert response.status_code == 200
    # assert response.json
