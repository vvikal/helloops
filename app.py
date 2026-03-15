from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

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
        "status" : "OK"
    })


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)