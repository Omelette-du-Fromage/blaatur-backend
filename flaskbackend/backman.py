import logging
from datetime import datetime

import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import requests as api_requests
import random

from flaskbackend import entur_api
from flaskbackend.constants import entur_journey_url, entur_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=["GET"])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route("/testing", methods=["POST"])
def data():
    # gets the "place" value from the HTTP body
    data_from_frontend = request.get_json()


    place_from = data_from_frontend.get("place_from", "")
    dest_blacklist: list = data_from_frontend.get("destinations_used", [])
    destination_candidates = ["Bergen", "Florø", "Arendal", "Voss", "Indre Arna", "Asker"]
    place_to = findRandomPlaceTo(place_from, destination_candidates, dest_blacklist)

    # Jeg refaktorerte dictet vi får tilbake, ettersom vi kan sende med "from" dataen i EnTur dataen.
    id_place_from = entur_api.place_getter(place_from)
    id_place_to = entur_api.place_getter(place_to)
    print(f'From: {id_place_from}')
    print(f'To: {id_place_to}')

    if id_place_from and id_place_to:
        entur_data = entur_api.journey_getter(id_place_from,
                                            id_place_to)

        databack = {}
        databack['trip'] = entur_data['data']['trip']['tripPatterns'][0]

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
        databack = entur_api.journey_getter(id_and_station_name_place_from['id'],
                                            id_and_station_name_place_to['id'])
        databack['name'] = id_and_station_name_place_to['name']
        return databack
    else:
        return "Record not found", 400

@app.route("/start", methods=["GET"])
def startingPoint():
    start = request.args.get("start")
    return jsonify([{"start": start}])


def findRandomPlaceTo(place_from, destination_candidates, dest_blacklist:list=[]):
    """Find a random place to go from list. If place_to and place_from is equal, find a new place."""
    dest_whitelist = [dest for dest in destination_candidates if dest not in dest_blacklist]
    place_to_candidate = random.choice(dest_whitelist)

    if(len(dest_whitelist) == 1 and (place_to_candidate in place_from)):
        return

    if len(dest_whitelist) <= 1:
        return findRandomPlaceTo(place_from, destination_candidates, [])
    elif place_to_candidate in place_from:
        return findRandomPlaceTo(place_from, destination_candidates, dest_blacklist)
    else:
        print(place_to_candidate)
        return place_to_candidate


# def aaaa():
#     # gets the "place" value from the HTTP body
#     # data_from_frontend = request.get_json()
#     place_from = "Bergen"
#     place_to = "Florø"
#
#     # Jeg refaktorerte dictet vi får tilbake, ettersom vi kan sende med "from" dataen i EnTur dataen.
#     id_place_from = entur_api.place_getter(place_from)
#     id_place_to = entur_api.place_getter(place_to)
#     print(f'From: {id_place_from}')
#     print(f'To: {id_place_to}')
#
#     if id_place_from and id_place_to:
#         databack = entur_api.journey_getter(id_place_from,
#                                             id_place_to)
#         return databack
#     else:
#         return "Record not found", 400
#
# print(aaaa())