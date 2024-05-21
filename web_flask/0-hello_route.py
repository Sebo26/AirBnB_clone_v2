#!/usr/bin/python3
from flask import Flask

web_flask = Flask(__name__)

@web_flask.route("/", strict_slashes=False)
def web_flask():
    return "<p>Hello HBNB!</p>"
