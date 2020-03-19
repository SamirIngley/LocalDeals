import googlemaps
import prettyprint
import os
import time
# from GoogleMapsAPIKey import get_my_key

# API_KEY = get_my_key()

#client - gateway to make requests and get requests back
gmaps = googlemaps.
Client(key = API_KEY)

#Define our search
places_result = gmaps.places_nearby(location='-33.8670522,151.1957362', radius = 40000, open_now = False, type = 'cafe')

pprint.pprint = (places_result)