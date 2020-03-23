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

# selenium help: https://www.youtube.com/watch?v=GJjMjB3rkJM
@app.route('/')
def geolocate():
    
    return render_template('geolocation.html')


# https://pythonise.com/series/learning-flask/flask-and-fetch-api
@app.route('/google', methods=["POST"])
def google_details():

    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "JSON received"}), 200)

    print(googled(req))
    print(res)

    return res


@app.route('/yelp')
def yelp():
    return yelped(), googled()