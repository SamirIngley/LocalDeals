import os
import sys
from subprocess import Popen, PIPE
from flask import Flask
from dotenv import load_dotenv
import googlemaps
import pprint
import time
import requests
import json
from operator import itemgetter

load_dotenv() # looks for dotenv file and driving variable names

def googled(coordinates):
    # KEY 
    google_key = os.environ.get("GOOGLE_API_KEY")
    
    # CLIENT
    gmaps = googlemaps.Client(key = google_key)

    # Define Search
    print(coordinates.values())

    coo = ''
    counter = 0
    for loc in coordinates.values():
        stringme = str(loc)
        coo += stringme
        if counter == 0:
            coo += ', '
        counter += 1

    print(coo)

    places_result = gmaps.places_nearby(location=coo, radius=10000, open_now=False, type="gym")

    # '37.2718841, -122.01945309999999'
    # pprint.pprint(places_result)

    # Get the next 20 results - pause it for 3 seconds to sync the timing
    # time.sleep(3)
    # places_result2 = gmaps.places_nearby(page_token = places_result['next_page_token'])

    # loop through each place in results, extract website

    details_list = []
    website_list = []

    for place in places_result['results']:
        my_place_id = place['place_id']
        my_fields = ['name', 'website', 'type']

        place_details = gmaps.place(my_place_id, fields = my_fields)
        details_list += (place_details)
        print('DETAILS ', place_details)
        print('RESULT ', place_details['result'])
        # print(place_details['result'].keys())
        if 'website' in place_details['result'].keys():
            print('WEBSITE ', place_details['result']['website'])
            website = place_details['result']['website']
            website_list.append(website)

    counter = 1
    for item in website_list:
        print(counter, item)
        counter += 1

    return 'hello'
