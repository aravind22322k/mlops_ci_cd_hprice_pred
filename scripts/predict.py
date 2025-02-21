import pickle
import numpy as np


# Load model
with open("/models/model.pkl", "rb") as f:
    model = pickle.load(f)


# Example prediction
def predict_price(input_data):
    return model.predict(np.array(input_data).reshape(1, -1))


# Example usage
if __name__ == "__main__":
    input_data = [2000, 3]  # Example: sqft=2000, bedrooms=3
    print(f"Predicted Price: {predict_price(input_data)[0]}")
