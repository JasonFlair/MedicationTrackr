#!/usr/bin/python3
"""Flask app"""
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sys
# set parent directory to avoid 
# attempted relative import with no known parent package error
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask_login import UserMixin, LoginManager
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/medicinedosetracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'notsosecretkey'
# mail configurations
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'medicationtrackrteam@gmail.com'
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = ('MedicationTrackr', 'medicationtrackrteam@gmail.com')
"""By providing a tuple with the desired name and the email address,
the MAIL_DEFAULT_SENDER configuration will be set accordingly. """
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# wrap flask mail and flask sqlalchemy around the flask app.
mail = Mail(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# aps scheduler
jobstore = {'default': SQLAlchemyJobStore(url=app.config['SQLALCHEMY_DATABASE_URI'])}
# enables persistency of jobs in case of shut down
scheduler = BackgroundScheduler(jobstores=jobstore, daemon=True)

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


# Start the scheduler
scheduler.start()
