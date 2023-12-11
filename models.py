from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    profile_image = db.Column(db.LargeBinary)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email_st = db.Column(db.String(120), unique=True, nullable=False)
    dept = db.Column(db.String(80), nullable=False)
    skills = db.Column(db.String(300))
    campus_st = db.Column(db.String(300))

# Add the following for debugging
print("Student model created")

class Company(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    company_logo = db.Column(db.LargeBinary)
    desc = db.Column(db.String(500), nullable=False)
    industry = db.Column(db.String(250), nullable=False)
    campus_cp = db.Column(db.String(300), nullable=False)
    website_url = db.Column(db.String(500))
    email_cp = db.Column(db.String(120), unique=True, nullable=False)
    company_size_min = db.Column(db.Integer)
    company_size_max = db.Column(db.Integer)

# Add the following for debugging
print("Company model created")
