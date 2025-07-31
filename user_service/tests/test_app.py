import pytest
from user_service.app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"User Service is running!" in response.data

def test_register_user(client):
    user_data = {
        "username": "testuser",
        "email": "test@example.com"
    }
    response = client.post('/register', json=user_data)
    assert response.status_code == 201
    assert response.get_json()["message"] == "User registered successfully"

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    users = response.get_json()
    assert isinstance(users, list)
