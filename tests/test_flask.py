import pytest
import json  # Add this import
from app import app  # Import the Flask app object


@pytest.fixture
def client():
    # Set up the test client
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_predict_endpoint(client):
    # Test the /predict endpoint
    response = client.post(
        "/predict",
        data=json.dumps({"input": [2000, 3]}),  # Serialize JSON payload
        content_type="application/json",  # Set content type to JSON
    )
    assert response.status_code == 200
    assert "predicted_price" in response.get_json()
