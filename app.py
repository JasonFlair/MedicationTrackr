#!/usr/bin/env python3
"""Flask app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/medicinedosetracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flask_login import UserMixin
from bcrypt import hashpw, checkpw, gensalt

class Medicine(db.Model):
  """Medicine class"""
  __tablename__ = 'medicines'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

class User(db.Model, UserMixin):
  """User class"""
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(40), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    password = password.encode()
    self.password = hashpw(password, gensalt())
    db.session.add(self)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
