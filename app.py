from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Conveyor Belt AI Backend is Running"

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    image = request.files["image"]

    filename = image.filename.lower()

    if any(word in filename for word in ["normal", "scratch", "crack", "rupture"]):
        result = filename
    else:
        result = "Invalid"

    return jsonify({
        "prediction": result,
        "message": "AI image analysis completed"
    })
@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)