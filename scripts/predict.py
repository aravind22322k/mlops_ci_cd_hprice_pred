import pickle
import pandas as pd

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_price(input_data):
    """Predict the price based on input sqft and bedrooms."""
    # Convert input to a DataFrame with correct feature names
    input_df = pd.DataFrame([input_data], columns=["sqft", "bedrooms"])
    prediction = model.predict(input_df)  # Model expects a DataFrame
 #  return float(prediction[0])  # Convert NumPy array to float
    return prediction.tolist()  # Convert NumPy array to list if necessary

# Example usage
if __name__ == "__main__":
    input_data = [2000, 3]  # Example: sqft=2000, bedrooms=3
    print(f"Predicted Price: {predict_price(input_data)}")
