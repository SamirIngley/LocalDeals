import os
from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from functools import reduce
from dotenv import load_dotenv
import googlemaps
import pprint
import time
import requests
import json

from googleapi import googled
from yelpapi import yelped
from scraper import search_site, website_list_loop

load_dotenv() # looks for dotenv file and driving variable names

app = Flask(__name__)


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/my_app_db')
client = MongoClient(host=f"{host}?retryWrites=false")
db = client.get_default_database()

search_history = db.history


# selenium help: https://www.youtube.com/watch?v=GJjMjB3rkJM
@app.route('/')
def geolocate():
    
    return render_template('geolocation.html')

@app.route('/', methods=['POST'])
def form_accept():
    """Make a new candy according to user's specifications."""
    search = {
        'prod': request.form.get('prod'),
        'cat': request.form.get('cat'),
        'rad': request.form.get('rad'),
        'open': request.form.get('open')
    }

    search_id = search_history.insert_one(search).inserted_id

    return redirect(url_for('google_details', search_id=search_id))


# https://pythonise.com/series/learning-flask/flask-and-fetch-api
@app.route('/google', methods=["POST"])
def google_details(search_id):

    req = request.get_json()
    print(req)

    res = make_response(jsonify({"message": "JSON received"}), 200)
    # print(res)

    # search = search_history.find_one({'_id': ObjectId(search_id)})
    # print(search)
    # print(search.open)

    # web_list = googled(req, str(search.cat), int(search.rad), bool(search.open))
    web_list = googled(req)
    print(googled(req))

    # website_list_loop(web_list, search.prod)
    website_list_loop(web_list, "mens jeans")


    return res


@app.route('/yelp')
def yelp():
    return yelped()