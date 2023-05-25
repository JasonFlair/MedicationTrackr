#!/usr/bin/python3
"""api views"""
from forms import RegistrationForm, LoginForm
from flask import jsonify, render_template, redirect, url_for, request
from api import User, Medicine, login_manager, db
from bcrypt import hashpw, checkpw, gensalt
from flask_login import login_user, login_required, logout_user, current_user

from flask import Blueprint
dosetracker_views = Blueprint('dosetracker_views', __name__)

def _hash_password(password):
  encoded_password = password.encode('utf-8')
  hashed_pw = hashpw(encoded_password, gensalt())
  return hashed_pw

# routes that handle authentication

@dosetracker_views.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      print('valid login')
      user = User.query.filter_by(email=form.email.data).first()
      print(user)
      if user:
        password = form.password.data
        print(password)
        encoded_password = password.encode('utf-8')
        if checkpw(encoded_password, user.password.encode('utf-8')):
            login_user(user)
            return redirect(url_for('dosetracker_views.dashboard'))
  return render_template('login.html', form=form)

@dosetracker_views.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  
  if form.validate_on_submit():
    print('yay!!!')
    hashed_pw = _hash_password(form.password.data)
    new_user = User(email=form.email.data,
                    username=form.username.data, 
                    password=hashed_pw)
    new_user.save()
    return redirect(url_for('dosetracker_views.login'))
  
    
  return render_template('register.html', form=form)

@dosetracker_views.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
  

# routes that handle other operations

@dosetracker_views.route('/current_user', methods=['GET', 'POST'],
                         strict_slashes=False)
@login_required
def current_user():
  this_user_id = current_user.id
  return jsonify({"user_id": this_user_id})

@dosetracker_views.route('/', methods=['GET', 'POST'],
                         strict_slashes=False)
def home():
  return 'Hello'

@dosetracker_views.route('/dashboard', methods=['GET', 'POST'],
                         strict_slashes=False)
@login_required
def dashboard():
    # store user id for operations
    user_id = current_user.id
    user_name = current_user.username
    return render_template('dashboard.html', user_id=user_id, user_name=user_name)
 
# routes for medicines operations 
@dosetracker_views.route('/new_medicine', methods=['GET', 'POST'])
def new_medicine():
  """adds new medicine"""
  data = request.get_json()
  user_id = data.get('user_id')
  name = data.get('name')
  quantity_per_dose = data.get('quantity')
  num_of_days = data.get('num_of_days')
  frequency = data.get('num_of_days')
  
  new_medicine = Medicine(name=name, user_id=user_id,
                          quantity=quantity_per_dose, num_of_days=num_of_days, frequency=frequency)
  new_medicine.save()
  new_medicine_details = {"name": name,
                          "user_id": user_id,
                          "quantity_per_dose": quantity_per_dose,
                          "num_of_days": num_of_days,
                          "frequency": frequency}
  return jsonify(new_medicine_details)

@dosetracker_views.route('/all_medicines_by_user/<id>', methods=['GET', 'POST'])
def get_all_medicines_by_user(id):
    user_id = int(id)
    medicines = Medicine.query.filter_by(user_id=user_id).all()
    medicines_list = []
    for medicine in medicines:
      medicine_obj = {}
      medicine_obj['name'] = medicine.name
      medicine_obj['user_id'] = medicine.user_id
      medicine_obj['quantity_to_be_taken'] = medicine.quantity
      medicine_obj['num_of_days'] = medicine.num_of_days
      medicine_obj['frequency'] = medicine.frequency
      medicine_obj['days_taken'] = medicine.days_taken
      medicine_obj['days_left'] = medicine.days_left
      
      medicines_list.append(medicine_obj)
    return jsonify({"medicines_for_user": medicines_list})