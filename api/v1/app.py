#!/usr/bin/python3
"""
This module contains the principal application
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app_host = getenv('HBNB_API_HOST', '0.0.0.0')
app.port = int(getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def close_db(obj):
    """ calls methods close() """
    storage.close()


@app.errorhandler(404)
def page_not_foun(error):
    """ Loads a custom 404 page not found """
    return jsonify(error= "Not found"), 404


@app.errorhandler(404)
def page_not_foun(error):
    """loads a custom 404 page not found"""
    msg = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        msg = error.description
    return jsonify(error=msg), 400


if __name__ == "__main__":
    app_host = getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = getenv('HBNB_API_PORT', '5000')

    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
