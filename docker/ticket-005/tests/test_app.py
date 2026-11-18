
import sys
from pathlib import Path

# Allow tests to import our Flask application
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()
    assert data["application"] == "ACME Financial"
    assert data["status"] == "running"


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
