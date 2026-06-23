from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Venterra Property API",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "property-api"
    })

@app.route("/properties")
def properties():
    return jsonify([
        {"id": 1, "name": "Richmond Hill Community", "status": "active"},
        {"id": 2, "name": "Toronto Residential Community", "status": "active"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
