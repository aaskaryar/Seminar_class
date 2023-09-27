import flask
from flask import render_template, request
import pandas as pd


app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    df = pd.read_csv(file)
    return render_template('view.html', data=df)