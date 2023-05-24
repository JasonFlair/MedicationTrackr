#!/usr/bin/env python3
"""Database module"""

class Db(db.Model):
  """db class"""
  def __init__(self):
    self._db = db
    self._db.create_all()
    
  def save(self, obj):
    """commit and save"""
    self._db.session.add(obj)
    self._db.session.commit()
    