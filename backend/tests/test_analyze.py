def test_analyze_with_file(client):
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


def test_analyze_result_can_be_retrieved(client):
    file_content = b"fake image data"

    response = client.post(
        "/analyze",
        files={
            "file": (
                "integration_test.png",
                file_content,
                "image/png"
            )
        }
    )

    assert response.status_code == 200

    analyze_data = response.json()
    job_id = analyze_data["job_id"]

    result_response = client.get(f"/results/{job_id}")

    assert result_response.status_code == 200

    result_data = result_response.json()

    assert result_data["job_id"] == job_id
    assert result_data["filename"] == "integration_test.png"
    assert result_data["prediction"] == "Normal"
    assert result_data["confidence"] == 0.85
    assert result_data["status"] == "completed"