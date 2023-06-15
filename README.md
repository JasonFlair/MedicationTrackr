# MedicationTrackr - a medicine dose tracker. Get it?

This is a webstack portfolio project by Favour Abangwu, Chukwuemelie Obumse and Afeez Abu.

Our project is a medicine dose tracker web app designed to help users in managing their medications effectively.

It offers a user-friendly interface with key features such as reminders, medication tracking and medication history. 

Our app aims to improve medication adherence, simplify medication management, and ultimately enhance users' health and well-being. With intuitive navigation and personalized email notifications our medicine dose tracker web app provides a seamless and efficient solution for users to stay on top of their medication regimen.

# Prerequisites

- Python
- Javascript
- React
- Flask
- Flask-Cors
- Flask-HTTPAuth
- Flask-Login
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Mail
- APScheduler
- Bcrypt

# Note: Check the requirements.txt file to install backend dependencies

# Built With:
- <a href="https://reactjs.org/" target="_blank">React</a>: React is a JavaScript library for building user interfaces. It provides a component-based architecture and efficiently renders and updates UI components, resulting in fast and interactive web applications. 
- <a href="https://flask.palletsprojects.com/" target="_blank">Flask</a>: A micro web framework for Python that provides a solid foundation for building web applications.
- <a href="https://flask-cors.readthedocs.io/" target="_blank">Flask-Cors</a>: An extension for Flask that simplifies Cross-Origin Resource Sharing (CORS) configuration.
- <a href="https://flask-httpauth.readthedocs.io/" target="_blank">Flask-HTTPAuth</a>: A Flask extension that provides basic and digest HTTP authentication for routes in your application.
- <a href="https://flask-login.readthedocs.io/" target="_blank">Flask-Login</a>: An extension for Flask that manages user authentication, including session management and remember me functionality.
- <a href="https://flask-sqlalchemy.palletsprojects.com/" target="_blank">Flask-SQLAlchemy</a>: An extension for Flask that simplifies database integration with SQLAlchemy, allowing you to interact with databases using Python objects.
- <a href="https://pythonhosted.org/Flask-Mail/" target="_blank">Flask-Mail</a>: An extension for Flask that provides a simple interface to send email messages from your application.
- <a href="https://apscheduler.readthedocs.io/" target="_blank">APScheduler</a>: A Python library that allows you to schedule jobs to be executed at specified intervals or times.
- <a href="https://pypi.org/project/bcrypt/" target="_blank">Bcrypt</a>: A password hashing library for Python that provides secure password storage and verification.

# Using the API:
The flask server can be started using the following commands:
`cd api`

`MAIL_ADDRESS='yourgoogleemail@gmail.com' MAIL_PASSWORD='yourgoogleapppassword' python3 -m app`
The mail address and mail password are used to authenticate with google's SMTP.

**Authentication**
A new user can be registered like so: 

`jason@Jason:~/medicine-dose-tracker$ curl -XPOST localhost:5000/register -H "Content-Type: application/json" -d '{"email": "name@email.com", "username": "Jay", "password": "password"}'`

The response will be a payload like this: 

{
  "email": "name@email.com",
  "id": 1,
  "username": "Jay"
}

The new user is saved to the database and addressed by the username in emails.

A login request can be made like so:
`curl -XPOST localhost:5000/login -H "Content-Type: application/json" -d '{"email": "name@email.com", "password": "password"}' -v`

The response will look like this:

* Mark bundle as not supporting multiuse

< HTTP/1.1 200 OK

< Server: Werkzeug/2.2.2 Python/3.8.10

< Date: Thu, 15 Jun 2023 11:46:44 GMT

< Content-Type: application/json

< Content-Length: 143

< Access-Control-Allow-Origin: *

< Vary: Cookie

< Set-Cookie: session=.eJwljjkOwzAMwP6iuYMk27KczwSODrRr0kxF_14D3Qgu5Af2PON6wvY-73jA_nLYoHYm8cZG1ETdpNeZ6V7LZAnKIdR0VCWSEajh6p0aZTs4FAsFyiCWiSgWaEv2odNczS2PmsZZOHOOQyRzkWsJ09UzaxMD1sh9xfm_Ifj-AJkEMAo.ZIr6JA.lTvcczIRFlNmDtRQV7lggT7Tkrw; HttpOnly; Path=/

< Connection: close

<

{
  "email": "emelieobumse123@gmail.com",
  "id": 1,
  "session_cookie details": "can be found in the verbose response",
  "username": "Jay"
}


For subsequent CRUD requests for medicine endpoints, a login is required, so be sure to pass in the session token gotten from the cookie in the login response.

**Dealing with the medicine endpoints**

To create a new medicine, the user's operation on the front end will call the /new_medicine endpoint, which should look like this in your command terminal:
`curl -XPOST 0.0.0.0:5000/new_medicine -H "Content-Type: application/json" -b 'session=.session_token_gotten_from_login;' -d '{"user_id": 1, "medicine_name": "Flagyl", "quantity": 1, "num_of_days": 5, "frequency": 3}'`

Here, quantity is the quantity per dose, frequency is the number of time such medicine is taken in a day and num_od_days is the number of days the medicine is to be taken.

The response expected should look like this:
{
  "created_at": "15-06-2023",
  "days_left": 5,
  "days_taken": 0,
  "frequency": 5,
  "medicine_id": 1,
  "medicine_name": "Flagyl",
  "num_of_days": 5,
  "quantity_per_dose": 1,
  "updated_at": "15-06-2023",
  "user_id": 1
}


To view all drugs stored by the user

`curl localhost:5000/all_medicines_by_user/1 -b 'session=.session_token_gotten_from_login;'`

Sample response:

{
  "medicines_for_user_1": [
    {
      "created_at": "15-06-2023",
      "days_left": 5,
      "days_taken": 0,
      "frequency": 5,
      "id": 1,
      "name": "Flagyl",
      "num_of_days": 5,
      "quantity_to_be_taken": 1,
      "updated_at": "15-06-2023",
      "user_id": 1
    },
    {
      "created_at": "15-06-2023",
      "days_left": 5,
      "days_taken": 0,
      "frequency": 5,
      "id": 3,
      "name": "Panadol",
      "num_of_days": 5,
      "quantity_to_be_taken": 2,
      "updated_at": "15-06-2023",
      "user_id": 1
    }
  ]
}

Updating medication status to communicate that the medicine has been taken completely for that day:

`curl -XPOST 0.0.0.0:5000/update_medication_status -H 'Content-Type: application/json' -d '{"user_id": 1, "day_completed": true, "name": "panadol"}' -b 'session=.session_token_gotten_from_login;'`

Sample response:

{
  "days_left": 4,
  "days_taken": 1
}


Deleting medicine:

`curl -XPOST 0.0.0.0:5000/delete_medicine -H "Content-Type: application/json" -b 'session=.session_token_gotten_from_login;' -d '{"user_id": 1, "medicine_id": 1}'`

Expected response:
{
  "status": "medicine deleted successfully"
}


# Contributors:

Frontend by Afeez Abu github - https://github.com/haffs_0

Backend by Chukwuemelie 'Jason Flair' Obumse. Email - emelieobumse100@gmail.com, Twitter - <a href="https://twitter.com/wfmjson" target="_blank"> My Twitter</a>. 