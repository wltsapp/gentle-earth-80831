import sys
import os
import flask
from flask import render_template, send_from_directory, request, redirect,url_for
from werkzeug import secure_filename
from flask import jsonify
import base64
import StringIO
#import tensorflow as tf 
import numpy as np
#import cv2
# Obtain the flask app object
app = flask.Flask(__name__)

UPLOAD_FOLDER='static'


@app.route('/')
def index():
    return "Webserver is running"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True, use_reloader=False)
