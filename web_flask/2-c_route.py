#!/usr/bin/python3
"""
Make Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
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


@app.route('/c/<text>')
def C_text():
    """
    Defines text
    """
    return "C" + text.replace("_", " ")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
