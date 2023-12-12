import os, jwt
from flask import jsonify

from app import app


@app.route("/", methods=['GET'])
def home():
    return jsonify({ "route": '/', "message": 'You are home'})

@app.errorhandler(404)
def routeNotFound(error):
    return jsonify({ "message": 'Route Not Found. Please Contact Developer'})

# @app.after_request
# def add_header(response):
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response