# dest_blacklist = ['Bergen', 'Asker']
# # destination_candidates = ['Bergen']
# #
# # x = all(dest in dest_blacklist for dest in destination_candidates)
# # print(x)
#
# x = any(dest in 'Bergen stasjon' for dest in dest_blacklist)
# print(x)

# gets the "place" value from the HTTP body
from flaskbackend import entur_api

place_from = "Bergen"
place_to = "Florø"

def testman():
    # gets the "place" value from the HTTP body
    data_from_frontend = request.get_json()

    place_from = data_from_frontend.get("place_from", "")
    dest_blacklist: list = data_from_frontend.get("destinations_used", [])
    destination_candidates = removeAlreadyVisitedPlacesFromList(dest_blacklist, ["Bergen", "Florø", "Arendal", "Voss", "Indre Arna", "Asker"])

    # Handle no more trips left
    if (len(destination_candidates) == 0):
        return "Record not found", 400

    # # Removes place_from from candidates
    # destination_candidates = [x for x in destination_candidates if x not in place_from]

    print(f'Dests: {destination_candidates}')

    place_to = findRandomPlaceTo(place_from, destination_candidates)

    # if not place_to: # I don't like this, Sam.
    #     place_to = findRandomPlaceTo(place_from, destination_candidates)


    # Jeg refaktorerte dictet vi får tilbake, ettersom vi kan sende med "from" dataen i EnTur dataen.
    id_place_from = entur_api.place_getter(place_from)
    id_place_to = entur_api.place_getter(place_to)
    print(f'From: {id_place_from}')
    print(f'To: {id_place_to}')

    if id_place_from and id_place_to:
        entur_data = entur_api.journey_getter(id_place_from,
                                              id_place_to)

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

testman()