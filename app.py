from flask import Flask, jsonify
import time

app = Flask(__name__)

count = 0

@app.route("/time")
def get_time():
    global count
    count += 1
    return jsonify({"time": int(time.time())})

@app.route("/metrics")
def get_metrics():
    return jsonify({"count": count})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
