#!/usr/bin/python

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5052/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False