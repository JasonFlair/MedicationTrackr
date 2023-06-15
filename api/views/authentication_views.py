#!/usr/bin/python3
"""authentication views"""
from flask import jsonify, request, abort, make_response
from api import app, mail
from api.models.users import User
from api.models.medicines import Medicine
from bcrypt import hashpw, checkpw, gensalt
from flask_mail import Message
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.exc import IntegrityError
import re

from api.views import dosetracker_views

# hashes password
def _hash_password(password):
    encoded_password = password.encode('utf-8')
    hashed_pw = hashpw(encoded_password, gensalt())
    return hashed_pw

# sends email using flask mail
def send_email(user_id, medicine_id):
   with app.app_context():
        medicine = Medicine.query.filter_by(user_id=user_id).filter_by(id=medicine_id).first()
        user = User.query.filter_by(id=user_id).first()
        if medicine.days_left > 0:
          msg = Message(subject="Remdinder to take your meds!", recipients=[user.email])
          msg.body = f"Dear {user.username}, \n\nPlease remember to take your medicine, {medicine.name}, the quantity per dose is {medicine.quantity} as usual. You have {medicine.days_left} day(s) left. \n\nLove, MedicationTrackr team."
          print (msg.body)
          mail.send(msg)

# routes that handle authentication

@dosetracker_views.route('/login', methods=['POST'])
def login():
    """login endpoint"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    if not email:
        return jsonify({"error": "no email sent"})
    if not password:
        return jsonify({"error": "no password sent"})
    print(user)
    if user:
        password = password
        encoded_password = password.encode('utf-8')
        if checkpw(encoded_password, user.password.encode('utf-8')):
            login_user(user)
            return jsonify({"username": f"{user.username}", "email": f"{user.email}", "id": user.id, "session_cookie details": "can be found in the verbose response"})
        else:
          error_json = jsonify(error="Unauthorised, wrong password")
          response = make_response(error_json, 401)
          abort(response)
    else:
      error_json = jsonify(error="Unauthorised, no user found")
      response = make_response(error_json, 401)
      abort(response)

@dosetracker_views.route('/register', methods=['POST'])
def register():
    try:
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        username = data.get('username')
        if not email:
          return jsonify({"error": "no email sent"})
        if not password:
          return jsonify({"error": "no password sent"})
        if not username:
          return jsonify({"error": "no password sent"})
        hashed_pw = _hash_password(password)
        # check if email is a valid email with regex
        if re.match(email_pattern, email) is not None:  # a match was found, email is valid.
            new_user = User(email=email,
                        username=username, 
                        password=hashed_pw)
            new_user.save()
            return jsonify({"username": f"{new_user.username}", "email": f"{new_user.email}", "id": new_user.id})
    except IntegrityError:
        return jsonify({"error": "attempting to register already existing user"})

@dosetracker_views.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return f'user logged out'
  
@dosetracker_views.route('/current_user', methods=['GET', 'POST'],
                         strict_slashes=False)
@login_required
def current_user():
  this_user_id = current_user.id
  return jsonify({"user_id": this_user_id})