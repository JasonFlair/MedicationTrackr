#!/usr/bin/python3
"""Flask app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
# set parent directory to avoid 
# attempted relative import with no known parent package error
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask_login import UserMixin, LoginManager
from bcrypt import hashpw, checkpw, gensalt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/medicinedosetracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'notsosecretkey'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# used to reload object from user id stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
  
  _db = db  
  def save(self):
      """saves and commits to database"""
      self._db.session.add(self)
      self._db.session.commit()

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
  
    

from views import dosetracker_views
app.register_blueprint(dosetracker_views)