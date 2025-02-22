import pytest
from app import app  # Ensure you're correctly importing the Flask app

@pytest.fixture
def client():
    return app.test_client()  # Correct way to initialize Flask's test client

def test_predict_endpoint(client):
    response = client.post("/predict", json={"input": [2000, 3]})
    assert response.status_code == 200
    assert "predicted_price" in response.get_json()
