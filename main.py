import logging
import datetime
from flask import Flask, render_template
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def hello():
    now = datetime.datetime.now()
    app.logger.info(str(now)+':Open Home Page')
    return render_template("index.html")


@app.route("/about")
def about():
    now = datetime.datetime.now()
    app.logger.info(str(now)+':Open About Page')
    return render_template("about.html")


@app.route("/contact")
def contact():
    now = datetime.datetime.now()
    app.logger.info(str(now)+':Open Contact Page')
    return render_template("contact.html")


@app.route("/gallery")
def gallery():
    now = datetime.datetime.now()
    app.logger.info(str(now)+':Open Gallery Page')
    return render_template("gallery.html")


@app.route("/facets")
def facets():
    now = datetime.datetime.now()
    app.logger.info(str(now)+':Open Facets Page')
    return render_template("facets.html")


if __name__ == "__main__":
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run()
