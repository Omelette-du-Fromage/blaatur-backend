import requests as api_requests
import json
from flaskbackend.constants import *

safe_header = {"ET-Client-Name": "blaatur-api", "Content-Type": "application/json"}


def journey_getter(place_from: str, place_to: str) -> dict:
    """
    Uses EnTur's "journey planner" api to fetch a trip from place to place.
    :param place_to:
    :return:
    """
    body = {
        "query": entur_query,
        "variables": {
            "frommann": place_from,
            "tomann": place_to,
        },
    }

    r = api_requests.post(entur_journey_url, json=body, headers=safe_header)
    x = r.json()
    return x


def place_getter(name):
    """
    Uses EnTur's "autocomplete" api to fetch stops from requested place.
    :param name: place we want to get Place ID from.
    :return: Place ID of place.
    """
    params = {"text": name, "size": "10", "lang": "en"}

    r = api_requests.get(entur_autocomp_url, params=params, headers=safe_header)
    x = r.json()

    # Currently only allows places with bus stations, e.g Bergen Stasjon, Voss Stasjon
    # Bus stations /= bus stops
    acceptable_results = ["busStation"]

    d = dict()

    for result in x["features"]:
        categories = result["properties"]["category"]
        if any(cat in acceptable_results for cat in categories):
            d['id'] = result["properties"]["id"]
            d['name'] = result["properties"]["name"]
            #print(result["properties"]["id"] + " ------")
            return d
