from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_results():
    response = client.get("/results")

    assert response.status_code == 200
    assert isinstance(response.json(), list) 

def test_get_result_by_job_id():
    job_id = "1bfa869b-3b5c-44f5-8610-00ecea8934a8"

    response = client.get(f"/results/{job_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["job_id"] == job_id
    assert "filename" in data
    assert "prediction" in data
    assert "confidence" in data
    assert "status" in data
    assert "timestamp" in data

def test_get_result_by_invalid_job_id():
    job_id = "00000000-0000-0000-0000-000000000000"

    response = client.get(f"/results/{job_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Result not found"}