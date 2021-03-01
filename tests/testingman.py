from flaskbackend.backman import app
from flask import request, jsonify


def test_api_start():
    with app.test_client() as c:
        rv = c.get('/testing', json={
            'email': 'flask@example.com', 'password': 'secret'
        })
        json_data = rv.get_json()
        name = "Voss"
        assert name == json_data[0]['start']