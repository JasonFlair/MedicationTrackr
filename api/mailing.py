#!/usr/bin/python3
"""deals with sending mails"""
from api import User, Medicine, app, mail
from flask_mail import Message

# sends email using flask mail
def send_email(user_id, medicine_id):
   with app.app_context():
        medicine = Medicine.query.filter_by(user_id=user_id).filter_by(id=medicine_id).first()
        user = User.query.filter_by(id=user_id).first()
        if medicine.days_left > 0:
          msg = Message(subject="Remdinder to take your meds!", recipients=[user.email])
          msg.body = f"Dear {user.username}, \nPlease remember to take your medicine, {medicine.name}, you have {medicine.days_left} day(s) left. \nLove, MDT team."
          print (msg.body)
          mail.send(msg)