import pytest
from app import app  # Import your Flask app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_endpoint(client):
    # Test the /predict endpoint
    response = client.post(
        "/predict",
        json={"input": [2000, 3]},  # Example input
    )
    assert response.status_code == 200
    assert "predicted_price" in response.get_json()
