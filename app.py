#!/usr/bin/env python3
"""Flask app"""
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models.user import User

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/medicinedosetracker'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
  app.run(debug=True)