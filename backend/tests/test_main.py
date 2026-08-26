def test_root(client):
    response = client.get("/")

    assert response.status_code == 200


def test_analyze_endpoint_no_file(client):
    response = client.post("/analyze")

    assert response.status_code == 422