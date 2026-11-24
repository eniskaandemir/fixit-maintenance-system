from app import create_app


def test_health_endpoint_returns_ok():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_home_endpoint_runs():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "FixIt"
    assert data["status"] == "running"
