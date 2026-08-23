from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_analyze_with_file():
    file_content = b"fake image data"

    response = client.post(
        "/analyze",
        files={
            "file": (
                "test.png",
                file_content,
                "image/png"
            )
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "job_id" in data
    assert data["status"] == "completed" 
