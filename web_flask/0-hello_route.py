from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def web_flask():
    return "<p>Hello HBNB!</p>"
