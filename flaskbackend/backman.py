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
    destination = ["Bergen", "Florø", "Arendal", "Voss", "Indre Arna", "Asker"]
    chosen = random.choice(destination)
    
    place_from = request.form.get("place_from")

    id_place_from = entur_api.place_getter(place_from)
    id_place_to = entur_api.place_getter(chosen)
    
    print(id_place_from)
    if (id_place_from):
        databack = entur_api.journey_getter(id_place_from['id'], id_place_to['id'])
        databack['name'] = id_place_from['name']

        return databack
    else:
        return "Record not found", 400


@app.route("/start", methods=["GET"])
def startingPoint():
    start = request.args.get("start")
    print(start)
    return jsonify([{"start": start}])
