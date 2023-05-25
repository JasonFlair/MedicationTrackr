#!/usr/bin/python3
from api import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
"""classes for signup/registration form and login form"""

class RegistrationForm(FlaskForm):
    """signup form"""
    email = StringField(validators=[InputRequired(), Length(min=6, max=35)],
                        render_kw={"placeholder": "Enter Email Address"})
    username = StringField(validators=[InputRequired(), Length(min=3, max=35)],
                        render_kw={"placeholder": "Pick a Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20), EqualTo('confirm', message='Passwords must match')],
                             render_kw={"placeholder": "New Password"})
    confirm = PasswordField(render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField("Register")
    def validate_email(self, email):
      existing_email = User.query.filter_by(email=email.data).first()
      if existing_email:
        raise ValidationError('Email already exists, login?')
  
class LoginForm(FlaskForm):
  """Login form"""
  email = StringField(validators=[InputRequired(), Length(min=6, max=35)],
                      render_kw={"placeholder": "Enter Email Address"})
  password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)],
                            render_kw={"placeholder": "Enter Password"})
  submit = SubmitField("Login")
  