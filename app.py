import os
from flask import Flask, render_template, redirect, url_for, request
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

@app.route('/')
def geolocate():
    
    return render_template('geolocation.html')


@app.route('/google')
def google_details():
    return googled()


@app.route('/yelp')
def yelp():
    return yelped()