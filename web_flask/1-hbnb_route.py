#!/usr/bin/python3
"""
Make Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Defines the home page
    """
    return "Hello HBNB!"
@app.route('/hbnb')
def hbnb():
    """
    Defines hbnb
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000
