from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/books": {"origins": "http://localhost:8080"}}, supports_credentials=True)
books = []

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    books.append(data)
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
