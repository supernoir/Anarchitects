#!/usr/bin/python

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5052/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False