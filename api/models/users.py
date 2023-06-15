#!/usr/bin/python3
"""Users module"""
from api import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  """User class"""
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(40), unique=True, nullable=False)
  username = db.Column(db.String(40), nullable=False)
  password = db.Column(db.String(80), nullable=False)
  _db = db  
  def save(self):
      """saves and commits to database"""
      self._db.session.add(self)
      self._db.session.commit()