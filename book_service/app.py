from flask import Flask, request, jsonify
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
CORS(app, resources={r"/books": {"origins": "http://localhost:8080"}}, supports_credentials=True)

# ✅ Enable Prometheus metrics
metrics = PrometheusMetrics(app)

books = []

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    books.append(data)
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

# Optional: simple home route
@app.route('/')
def home():
    return "Book Service is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
