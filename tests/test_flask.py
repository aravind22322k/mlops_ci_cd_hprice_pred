import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    response = client.post("/predict", json={"input": [2000, 3]})
    assert response.status_code == 200
    assert "predicted_price" in response.json
