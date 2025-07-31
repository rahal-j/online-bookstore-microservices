from order_service.app import app  # or book_service.app if testing that one

def test_users_get():
    client = app.test_client()
    response = client.get('/users')
    assert response.status_code == 200
