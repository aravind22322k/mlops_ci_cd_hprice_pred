import pytest
from scripts.predict import predict_price


def test_predict_price():
    input_data = [2000, 3]
    predicted_price = predict_price(input_data)
    assert isinstance(predicted_price, float), (
        "Prediction should be a float value"
    )
