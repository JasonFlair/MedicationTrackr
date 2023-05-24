#!/usr/bin/env python3
"""Medicine module"""


class Medicine(db.Model):
  """Medicine class"""
  __tablename__ = 'medicines'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 