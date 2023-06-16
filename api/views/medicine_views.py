#!/usr/bin/python3
"""api views"""
from flask import jsonify, request
from api import app, mail, scheduler
from api.models.users import User
from api.models.medicines import Medicine
from flask_mail import Message
from flask_login import login_required, current_user
from datetime import datetime

from api.views import dosetracker_views

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

 
# routes for medicines operations 
@dosetracker_views.route('/new_medicine', methods=['GET', 'POST'])
@login_required
def new_medicine():
  """adds new medicine"""
  data = request.get_json()
  user_id = data.get('user_id')
  medicine_name = data.get('medicine_name')
  quantity_per_dose = data.get('quantity')
  num_of_days = data.get('num_of_days')
  frequency = data.get('num_of_days')
  days_taken = 0
  days_left = num_of_days
  created_at = datetime.now().strftime('%d-%m-%Y')
  updated_at = datetime.now().strftime('%d-%m-%Y')
  
  
  new_medicine = Medicine(name=medicine_name, user_id=user_id,
                          quantity=quantity_per_dose,
                          num_of_days=num_of_days,
                          frequency=frequency,
                          days_left= days_left, days_taken=days_taken,
                          created_at=created_at, updated_at=updated_at)
  new_medicine.save()

  new_medicine_details = {"medicine_name": medicine_name,
                          "user_id": user_id,
                          "quantity_per_dose": quantity_per_dose,
                          "num_of_days": num_of_days,
                          "frequency": frequency,
                          "days_taken": days_taken,
                          "days_left": days_left,
                          "medicine_id": new_medicine.id,
                          "created_at": new_medicine.created_at,
                          "updated_at": new_medicine.updated_at}
  # schedule a job to send email reminders every 9 hours
  scheduler.add_job(send_email, 'interval', hours=9, kwargs={'user_id':user_id, 'medicine_id': new_medicine.id})
  return jsonify(new_medicine_details)

@dosetracker_views.route('/all_medicines_by_user/<id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
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
      medicine_obj['id'] = medicine.id
      medicine_obj['created_at'] = medicine.created_at
      medicine_obj['updated_at'] = medicine.updated_at
      
      medicines_list.append(medicine_obj)
    return jsonify({f"medicines_for_user_{user_id}": medicines_list})
  
@dosetracker_views.route('/update_medication_status', methods=['POST'], strict_slashes=False)
@login_required
def update_medication_status():
  data = request.get_json()
  user_id = data.get('user_id')
  medicine = data.get('name')
  day_completed = data.get('day_completed')
  
  if day_completed == True:
    try:
        medicine_to_be_updated = Medicine.query.filter_by(
            user_id=user_id).filter_by(name=medicine).first()
        days_left = medicine_to_be_updated.days_left
        days_taken = medicine_to_be_updated.days_taken
        
        # update days taken and days left
        new_days_left = days_left - 1
        new_days_taken = days_taken + 1
        medicine_to_be_updated.days_left = new_days_left
        medicine_to_be_updated.days_taken = new_days_taken
        medicine_to_be_updated.updated_at = datetime.now().strftime('%d-%m-%Y')
        Medicine.save(medicine_to_be_updated)
        return jsonify({"days_left": new_days_left, "days_taken": new_days_taken})
    except Exception:
        return jsonify({"error": "no medicine found, please check your payload details"})
    
@dosetracker_views.route('/delete_medicine', methods=['POST'], strict_slashes=False)
@login_required
def delete_medicine():
    """deletes medicine specified"""
    data = request.get_json()
    user_id = data.get('user_id')
    medicine_id = data.get('medicine_id')
    try:
        medicine_to_be_deleted = Medicine.query.filter_by(
      user_id=user_id).filter_by(id=medicine_id).first()
        Medicine.delete(medicine_to_be_deleted)
        return jsonify({"status": "medicine deleted successfully"})
    except Exception:
        return jsonify({"error": f"no medicine with medicine_id and user_id found"})
      