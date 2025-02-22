# tests/test_model.py
from scripts.predict import predict_price  # Import predict_price from scripts/predict.py


def test_predict_price():
    # Test the predict_price function
    input_data = [2000, 3]  # Example input
    prediction = predict_price(input_data)
    assert isinstance(prediction, float)  # Ensure the prediction is a float
