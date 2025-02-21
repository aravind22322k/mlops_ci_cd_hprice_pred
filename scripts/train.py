import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


# Load data
data = pd.read_csv("data/housing.csv")  # Path relative to repository root
X = data.drop("price", axis=1)
y = data["price"]


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Save model
with open("models/model.pkl", "wb") as f:  # Path relative to repository root
    pickle.dump(model, f)


print("Model trained and saved!")
