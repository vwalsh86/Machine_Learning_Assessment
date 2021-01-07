# How to run flask on Windows via Command Prompt
# set FLASK_APP=rando.py
# python -m flask run

import flask as fl
import numpy as np

from tensorflow.keras.models import model_from_json

from flask import Flask

#Create a new web app.
app = fl.Flask(__name__)


@app.route("/")
def home():
  return ("index.html")

if __name__ == "__main__":
    app.run(debug= True) 