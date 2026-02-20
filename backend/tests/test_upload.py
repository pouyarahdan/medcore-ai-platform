from fastapi.testclient import TestClient
from backend.main import app
import io

client = TestClient(app)

def test_upload_image():
    file_content = b"fake image data"
    file = io.BytesIO(file_content)

    response = client.post(
        "/upload-image/",
        files={"file": ("test.png", file, "image/png")}
    )

    assert response.status_code == 200
    assert response.json()["filename"] == "test.png"
    assert response.json()["message"] == "Image uploaded successfully"