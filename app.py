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
        coords = request.get_json()
        print('home coords: ', coords)

        res = make_response(jsonify({"message": "JSON received"}), 200)

        params = {
            'product' : request.form.get('prod'),
            'category' : request.form.get('cat'),
            'radius' : request.form.get('rad'),
            'opennow' : request.form.get('open'),
        }
        
        print(params.items())
        
        return 'hi'


    
    return render_template('geolocation.html')


# https://pythonise.com/series/learning-flask/flask-and-fetch-api
@app.route('/google', methods=["GET", "POST"])
def google_details():

    return res


@app.route('/yelp')
def yelp():
    return yelped(), googled()