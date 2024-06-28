from . import db #importing from the current package(website which has been initialsied using __init__ which gives access to __init__.py)
from flask_login import UserMixin 
from sqlalchemy.sql import func # imports sql functions as we use func.now() to get the current time


class Note(db.Model): #this class inherits from db.Model class
    id = db.Column(db.Integer,primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model,UserMixin): #inherits from both db.Model, and UserMixin
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150),unique=True)#makes the email column completely unique
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


