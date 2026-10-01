import io


def test_upload_image(client):
    file_content = b"fake image data"
    file = io.BytesIO(file_content)

    response = client.post(
        "/upload-image/",
        files={"file": ("test.png", file, "image/png")}
    )

    assert response.status_code == 200
    assert response.json()["filename"] == "test.png"
    assert response.json()["message"] == "Image uploaded successfully"


def test_upload_invalid_file_type(client):
    file_content = b"this is not an image"
    file = io.BytesIO(file_content)

    response = client.post(
        "/upload-image/",
        files={"file": ("test.txt", file, "text/plain")}
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Unsupported file type"
    }


def test_upload_empty_file(client):
    file = io.BytesIO(b"")

    response = client.post(
        "/upload-image/",
        files={"file": ("empty.png", file, "image/png")}
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Empty file"
    }