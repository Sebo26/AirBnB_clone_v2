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
def c_text(text):
    """
    Defines text route, replacing underscores with spaces
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_text(text):
    """
    Defines python text route,replacing underscores with spaces
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """
    Defines a number if it is an integer
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n)
    """
    Defines HTML page number
    """
    return f"<h1>Number: {n}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
