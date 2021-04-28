import logging
from datetime import datetime

import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import requests as api_requests
import random

from flaskbackend import entur_api

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["GET"])
def home():
    return "<h1>Empty page</h1><p>Try POSTing { \"place_from\": \"Bergen\", \"destinations_used\": [] } to /get_blaatur instead.</p>"



@app.route("/get_blaatur", methods=["POST"])
@cross_origin()
def data():
    # gets the "place" value from the HTTP body
    data_from_frontend = request.get_json()

    place_from = data_from_frontend.get("place_from", "")
    dest_blacklist: list = data_from_frontend.get("destinations_used", [])
    start_date = data_from_frontend.get("start_date", datetime.now())
    destination_candidates = removeAlreadyVisitedPlacesFromList(dest_blacklist, ["Bergen", "Florø", "Arendal", "Voss", "Indre Arna", "Asker"])

    # Handle no more trips left
    if (len(destination_candidates) == 0):
        return "Record not found", 400

    # # Removes place_from from candidates
    # destination_candidates = [x for x in destination_candidates if x not in place_from]

    print(f'Dests: {destination_candidates}')

    place_to = findRandomPlaceTo(place_from, destination_candidates)

    # Jeg refaktorerte dictet vi får tilbake, ettersom vi kan sende med "from" dataen i EnTur dataen.
    id_place_from = entur_api.place_getter(place_from)
    id_place_to = entur_api.place_getter(place_to)
    print(f'From: {id_place_from}')
    print(f'To: {id_place_to}')

    if id_place_from and id_place_to:
        entur_data = entur_api.journey_getter(id_place_from,
                                             id_place_to, destination_candidates,
                                             startDate=start_date)

        if (entur_data == None):
            return "Record not found", 404
        databack = {}
        databack['trip'] = entur_data['data']['trip']['tripPatterns'][0]

        if place_to not in dest_blacklist:
            dest_blacklist.append(place_to)
        databack['destinations_used'] = dest_blacklist
        return databack
    else:
        return "Record not found", 400

def dataHasTrip(trip):
    return len(trip['data']['trip']['tripPatterns']) != 0


@app.route("/mockPlaceTo", methods=["POST"])
def dataMock():
    # gets the "place" value from the HTTP body
    place_from = "Bergen"
    place_to = "Florø"

    id_and_station_name_place_from = entur_api.place_getter(place_from)
    id_and_station_name_place_to = entur_api.place_getter(place_to)
    print(f'From: {id_and_station_name_place_from}')
    print(f'To: {id_and_station_name_place_to}')

    if id_and_station_name_place_from and id_and_station_name_place_to:
        databack = entur_api.journey_getter(id_and_station_name_place_from,
                                            id_and_station_name_place_to)
        databack['name'] = id_and_station_name_place_to
        return databack
    else:
        return "Record not found", 400

@app.route("/start", methods=["GET"])
def startingPoint():
    start = request.args.get("start")
    return jsonify([{"start": start}])


def findRandomPlaceTo(place_from, destination_candidates):
    """Find a random place to go from list. If place_to and place_from is equal, find a new place."""
    place_to_candidate = random.choice(destination_candidates)
    if place_to_candidate in place_from:
        return findRandomPlaceTo(place_from, destination_candidates)
    else:
        return place_to_candidate

# SRP
def removeAlreadyVisitedPlacesFromList(placesToRemove, places):
    placesToRemoveSet = set(placesToRemove)
    placesToGoSet = set(places)
    return list(placesToGoSet.difference(placesToRemoveSet))
