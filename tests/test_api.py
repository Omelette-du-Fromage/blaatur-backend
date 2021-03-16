from flaskbackend.backman import app
import flaskbackend.backman as backman


def test_api_start():
    app.testing = True
    with app.test_client() as c:
        rv = c.post("/testing",  json={"place_from": "Bergen"}, headers={"Content-Type": "application/json"})
        assert rv is not None


def test_find_random_place_to():
    app.testing = True
    place_from = "Bergen busstasjon"
    places_to_go = ["Bergen"]
    assert backman.findRandomPlaceTo(place_from, places_to_go) is None

def test_findRandomPlace_to_should_return_place_to_when_availiable():
    app.testing = True 
    place_from = "Arendal Busstasjon"
    places_to_go = ["Bergen", "Arendal"]
    assert backman.findRandomPlaceTo(place_from, places_to_go) == "Bergen"

def test_no_trip():
    app.testing = True
    data = {
            "data":
            {
            "trip":
                {"debugOutput":
                    {
                    "totalTime": 1227
                    },
                    "tripPatterns": []
                }
            },
             "name": "Florø rutebilstasjon"
            }
    assert backman.dataHasTrip(data) == False
    