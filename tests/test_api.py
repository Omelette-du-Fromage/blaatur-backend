from flaskbackend.backman import app
import flaskbackend.backman as backman

def test_api_start():
    app.testing = True
    with app.test_client() as c:
        rv = c.post("/testing",  json={"place_from": "Bergen"}, headers={"Content-Type": "application/json"})
        assert rv is not None


def testFindRandomPlaceTo():
    app.testing = True
    place_from = "Bergen busstasjon"
    places_to_go = ["Bergen"]
    assert backman.findRandomPlaceTo(place_from, places_to_go) is None

