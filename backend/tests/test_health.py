from unittest.mock import MagicMock
from sqlalchemy.exc import OperationalError

from backend.main import app
from backend.database.database import get_db


def test_health_check_success(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "connected"
    }


def test_health_check_database_failure(client):
    mock_db = MagicMock()

    mock_db.execute.side_effect = OperationalError(
        "SELECT 1",
        {},
        Exception("Database connection failed")
    )

    def override_get_db():
        yield mock_db

    original_override = app.dependency_overrides.get(get_db)

    app.dependency_overrides[get_db] = override_get_db

    try:
        response = client.get("/health")

        assert response.status_code == 503
        assert response.json() == {
            "detail": "Database unavailable"
        }

    finally:
        if original_override is None:
            app.dependency_overrides.pop(get_db, None)
        else:
            app.dependency_overrides[get_db] = original_override