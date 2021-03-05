import flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import requests as api_requests

from flaskbackend import entur_api
from flaskbackend.constants import entur_journey_url, entur_query

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cors = CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/testing', methods=['GET'])
def data():
# gets the "place" value from the HTTP body, defaults to Voss if none exists.
    place = request.form.get('place', default='Voss')

    databack = entur_api.journey_getter(place)

    response = databack
    return response

@app.route('/start', methods=['GET'])
def startingPoint():
    start = request.args.get('start')
    print(start)
    return jsonify([{"start":start}])
    

