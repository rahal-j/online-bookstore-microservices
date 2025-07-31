from book_service.app import app

def test_books_get():
    client = app.test_client()
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_books_post():
    client = app.test_client()
    response = client.post('/books', json={"id": 1, "title": "Test Book"})
    assert response.status_code == 201
    assert response.get_json()["message"] == "Book added successfully"
