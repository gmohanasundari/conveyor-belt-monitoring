from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Conveyor Belt AI Backend is Running"

@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"})

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files["image"]
    filename = image.filename.lower()

    if "normal" in filename:
        result = "Normal"
    elif "scratch" in filename:
        result = "Scratch"
    elif "crack" in filename:
        result = "Crack"
    elif "rupture" in filename:
        result = "Rupture"
    else:
        result = "Invalid"

    return jsonify({
        "prediction": result,
        "message": "AI image analysis completed"
    })

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
