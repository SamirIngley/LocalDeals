import os
from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from dotenv import load_dotenv
import googlemaps
import pprint
import time
import requests
import json
 
from googleapi import googled
from yelpapi import yelped

load_dotenv() # looks for dotenv file and driving variable names

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def geolocate():

    if request.method == "POST":

        req = request.get_json()
        # print(type(req))
        lat = req['lat']
        lng = req['lng']
        prod = req['prod']
        cat = req['cat']
        rad = req['rad']
        now = req['now']
        # print(prod)
        # res = make_response(jsonify({"message": "JSON received"}), 200)
        # res = make_response(jsonify(req), 200)

        return redirect(url_for('google_details', req=req, lat=lat, lng=lng, prod=prod, cat=cat, rad=rad, now=now))

    
    return render_template('geolocation.html')


# https://pythonise.com/series/learning-flask/flask-and-fetch-api
@app.route('/google/<req>/<lat>/<lng>/<prod>/<cat>/<rad>/<now>', methods=["POST", "GET"])
def google_details(req, lat, lng, prod, cat, rad, now):

    # print('getme', type(req))
    # print(req)
    # print(lat, lng, type(lat))
    print(prod, cat, rad, now, type(prod))
    # print('LAT LNG ', req[lat], req[lng])
    googled(req, lat, lng, prod, cat, rad, now)

    return 'hi'


@app.route('/yelp')
def yelp():
    return yelped(), googled()