from flaskbackend.backman import app
from flask import request, jsonify


def test_api_start():
    app.testing = True
    with app.test_client() as c:
        rv = c.get("/testing")
        json_data = rv.get_json()
        assert json_data[0]["start"] is not None


def test_api_can_get_start_value():
    app.testing = True
    with app.test_client() as client:
        req = client.get("/start?start=hei")
        assert request.args.get("start") is not None
