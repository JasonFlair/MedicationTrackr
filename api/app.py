#!/usr/bin/python3
"""Flask app"""
import os
import sys
# set parent directory to avoid 
# attempted relative import with no known parent package error
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
