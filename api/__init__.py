#!/usr/bin/python3
"""Flask app"""
from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
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
MAIL_ADDRESS = getenv('MAIL_USERNAME')
app.config['MAIL_USERNAME'] = MAIL_ADDRESS
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = ('MedicationTrackr', f'{MAIL_ADDRESS}')
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
    from api.models.users import User
    return User.query.get(int(user_id)) 
    
#import blue print
from api.views import dosetracker_views
# import all views
from api.views.authentication_views import *
from api.views.medicine_views import *
app.register_blueprint(dosetracker_views)


# Start the scheduler
scheduler.start()
scheduler.remove_all_jobs()