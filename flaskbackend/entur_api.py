import requests as api_requests
import json
from flaskbackend.constants import *
from datetime import datetime
from dateutil import parser

safe_header = {"ET-Client-Name": "blaatur-api", "Content-Type": "application/json"}


def journey_getter(place_from: str, place_to: str, startDate=datetime.now()) -> dict:
    """
    Uses EnTur's "journey planner" api to fetch a trip from place to place.
    Currently runs a while-loop with continous 400 minute search window API requests.
    :param place_to:
    :return:
    """

    while True:
        body = {
            "query": entur_query,
            "variables": {
                "frommann": place_from,
                "tomann": place_to,
                "dateTime": startDate.astimezone().replace(microsecond=0).isoformat()
            }
        }

        response = api_requests.post(entur_journey_url, json=body, headers=safe_header)
        trip_json = response.json()

        print(trip_json)
        print(trip_json['data']['trip'])

        if trip_json['data']['trip'] == None:
            return None
        if not trip_json['data']['trip']['tripPatterns']:
            date_data = trip_json['data']['trip']['metadata']['nextDateTime']
            startDate = parser.parse(date_data)
        else:
            return trip_json


def place_getter(name):
    """
    Uses EnTur's "autocomplete" api to fetch stops from requested place.
    :param name: place we want to get Place ID from.
    :return: Place ID of place.
    """
    params = {"text": name, "size": "10", "lang": "en"}

    response = api_requests.get(entur_autocomp_url, params=params, headers=safe_header)
    entur_json = response.json()

    # Currently only allows places with bus stations, e.g Bergen Stasjon, Voss Stasjon
    # Bus stations /= bus stops
    acceptable_results = ['busStation', 'railStation', 'onstreetBus']


    for result in entur_json["features"]:
        categories = result["properties"]["category"]

        if any(cat in acceptable_results for cat in categories):
            return result["properties"]["id"]
