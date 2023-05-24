#!/usr/bin/env python3
"""User module"""
from app import db
from flask_login import UserMixin

class User(db.model):
  """User class"""