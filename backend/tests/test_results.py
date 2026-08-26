def test_get_results(client):
    response = client.get("/results")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_result_by_job_id(client):
    analyze_response = client.post(
        "/analyze",
        files={
            "file": (
                "result_test.png",
                b"fake image data",
                "image/png"
            )
        }
    )

    assert analyze_response.status_code == 200

    job_id = analyze_response.json()["job_id"]

    response = client.get(f"/results/{job_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["job_id"] == job_id
    assert data["filename"] == "result_test.png"
    assert "prediction" in data
    assert "confidence" in data
    assert data["status"] == "completed"
    assert "timestamp" in data


def test_get_result_by_invalid_job_id(client):
    job_id = "00000000-0000-0000-0000-000000000000"

    response = client.get(f"/results/{job_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Result not found"}