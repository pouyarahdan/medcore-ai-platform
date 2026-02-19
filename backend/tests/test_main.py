from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_analyze_endpoint_no_file():
    response = client.post("/analyze")
    assert response.status_code == 422 