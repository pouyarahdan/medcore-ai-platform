from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_results():
    response = client.get("/results")

    assert response.status_code == 200
    assert isinstance(response.json(), list) 
