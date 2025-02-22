from scripts.predict import predict_price


def test_predict_price():
    """Test the predict_price function."""
    input_data = [2000, 3]  # Example input (sqft, bedrooms)
    prediction = predict_price(input_data)

    # Ensure the prediction is a float
    assert isinstance(prediction, float), f"Expected float, got {type(prediction)}"

    # Ensure prediction is within a reasonable range
    assert prediction > 0, f"Expected positive price prediction, got {prediction}"
