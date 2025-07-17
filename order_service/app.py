from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

orders = []

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    # fetch user list (simulate lookup)
    users = requests.get("http://user-service:5000/users").json()
    # (optional) check if user exists
    return jsonify({"message": "Order placed", "user_check": users}), 201

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
