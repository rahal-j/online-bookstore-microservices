from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app)

# ✅ Enable Prometheus metrics
metrics = PrometheusMetrics(app)

orders = []

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json

    try:
        users = requests.get("http://user-service:5000/users").json()
    except Exception as e:
        return jsonify({"message": "User service unreachable", "error": str(e)}), 500

    orders.append(data)
    return jsonify({"message": "Order placed", "user_check": users}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

@app.route('/')
def home():
    return "Order Service is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
