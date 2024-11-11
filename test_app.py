# test_app.py
import app
import pytest

# Enable testing mode
app.app.testing = True
client = app.app.test_client()

def test_add():
    response = client.get('/add?a=2&b=3')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 5

def test_invalid_input():
    response = client.get('/add?a=two&b=3')
    data = response.get_json()
    assert response.status_code == 400
    assert 'error' in data
