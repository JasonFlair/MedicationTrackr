#!/usr/bin/python3
"""Medicines module"""
from api import db

class Medicine(db.Model):
  """Medicine class"""
  __tablename__ = 'medicines'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  num_of_days = db.Column(db.Integer, nullable=False)
  frequency = db.Column(db.Integer, nullable=False)
  days_taken = db.Column(db.Integer)
  days_left = db.Column(db.Integer)
  created_at = db.Column(db.String(20), nullable=False)
  updated_at = db.Column(db.String(20), nullable=False)
  
  _db = db  
  def save(self):
      """saves and commits to database"""
      self._db.session.add(self)
      self._db.session.commit()
      
  def delete(self):
    """deletes an objects and commits to database"""
    self._db.session.delete(self)
    self._db.session.commit()