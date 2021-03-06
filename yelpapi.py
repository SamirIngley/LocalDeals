import os
from flask import Flask
from dotenv import load_dotenv
import googlemaps
import pprint
import time
import requests
import json

#Business Search      URL -- 'https://api.yelp.com/v3/businesses/search'
#Business Match       URL -- 'https://api.yelp.com/v3/businesses/matches'
#Phone Search         URL -- 'https://api.yelp.com/v3/businesses/search/phone'

#Business Details     URL -- 'https://api.yelp.com/v3/businesses/{id}'
#Business Reviews     URL -- 'https://api.yelp.com/v3/businesses/{id}/reviews'

#Businesses, Total, Region

def yelped():
    # Define a business ID
    business_id = '4AErMBEoNzbk7Q8g45kKaQ'
    unix_time = 1546047836

    # Define my API Key, My Endpoint, and My Header
    yelp_key = os.environ.get("YELP_API_KEY")
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

    # ENDPOINT = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id)
    HEADERS = {'Authorization': 'bearer %s' % yelp_key}

    # Define my parameters of the search
    # BUSINESS SEARCH PARAMETERS - EXAMPLE
    PARAMETERS = {

                'term': 'coffee',
                'limit': 50,
                'offset': 50,
                # 'longitude': 37.2638,
                # 'latitude': 122.0230,
                'radius': 10000,
                'location': 'Saratoga'

                }

    # BUSINESS MATCH PARAMETERS - EXAMPLE
    #PARAMETERS = {'name': 'Peets Coffee & Tea',
    #              'address1': '7845 Highland Village Pl',
    #              'city': 'San Diego',
    #              'state': 'CA',
    #              'country': 'US'}

    # Make a request to the Yelp API
    response = requests.get(url = ENDPOINT,
                            params = PARAMETERS,
                            headers = HEADERS)
    # print the response
    # print(json.dumps(business_data, indent = 3))
    
    # Conver the JSON String
    business_data = response.json()
    for biz in business_data['businesses']:
        print(biz)


    return 'Yelp'