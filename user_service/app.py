from flask import Flask, request, jsonify
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app, origins="http://localhost:8080", supports_credentials=True)

# ✅ Add Prometheus monitoring
metrics = PrometheusMetrics(app)

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/')
def home():
    return "User Service is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
