import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import requests as api_requests
import random

from flaskbackend import entur_api
from flaskbackend.constants import entur_journey_url, entur_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route("/testing", methods=["POST"])
def data():
    # gets the "place" value from the HTTP body
    destination = ["Bergen", "Florø", "Arendal", "Voss", "Indre Arna", "Asker"]
    chosen = random.choice(destination)

    place_from = request.form.get("place_from", default="Bergen")

    databack = entur_api.journey_getter("Voss")

    print(entur_api.place_getter(place_from))

    response = databack
    return response


@app.route("/start", methods=["GET"])
def startingPoint():
    start = request.args.get("start")
    print(start)
    return jsonify([{"start": start}])
