from flask import Flask, request, jsonify
from scripts.predict import predict_price

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    input_data = data["input"]
    prediction = predict_price(input_data)
    return jsonify({"predicted_price": prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
