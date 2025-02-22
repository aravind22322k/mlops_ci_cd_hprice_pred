import numpy as np


def predict_price(input_data):
    """
    Predict the price based on input data.
    """

    # Example model logic (replace with actual model inference)
    prediction = np.mean(input_data) * 1000
 
    return prediction


# Ensure the script runs correctly when executed
if __name__ == "__main__":
    sample_input = [2000, 3]
    print(predict_price(sample_input))
