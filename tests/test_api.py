from flaskbackend.backman import app

def test_api_start():
    app.testing = True
    with app.test_client() as c:
        rv = c.post("/testing",  json={"place_from": "Bergen"}, headers={"Content-Type": "application/json"})
        assert rv is not None
