from flask import Flask, jsonify
from datetime import datetime
import os

from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "helloops_requests_total",
    "Total HTTP requests to helloops"
)

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route("/")
def home():
    api_key_present = bool(os.getenv("APP_API_KEY"))

    return jsonify({
        "app": "helloops",
        "version": os.getenv("APP_VERSION", "v1"),
        "environment": os.getenv("APP_ENV", "dev"),
        "api_key_present": api_key_present,
        "time": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)