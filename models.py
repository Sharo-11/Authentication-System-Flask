from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Student(db.Model, UserMixin):
    st_id = db.Column(db.Integer, primary_key = True)
    st_username = db.Column(db.String(20), nullable = False, unique = True)
    st_password = db.Column(db.String(80), nullable = False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    st_email = db.Column(db.String(100), unique=True, nullable=False)
    st_campus = db.Column(db.String(100), nullable=False)
    st_department = db.Column(db.String(100), nullable=False)
    st_year = db.Column(db.Integer, nullable=False)
    st_profile_pic = db.Column(db.String(100))

class Company(db.Model, UserMixin):
    cp_id = db.Column(db.Integer, primary_key=True)
    cp_username = db.Column(db.String(20), nullable = False, unique = True)
    cp_password = db.Column(db.String(80), nullable = False)
    cp_name = db.Column(db.String(40), nullable = False)
    cp_desc = db.Column(db.String(500), nullable = False)
    cp_industry = db.Column(db.String(30), nullable = False)
    cp_website = db.Column(db.String(100), nullable = False)
    cp_email = db.Column(db.String(20), nullable = False)
    cp_contact = db.Column(db.Integer, nullable = False)
    cp_primary_contact = db.Column(db.Integer, nullable = False)
    cp_size = db.Column(db.String(20), nullable = False)
    cp_campus = db.Column(db.String(40), nullable = False)
    cp_logo = db.Column(db.String(100), nullable = False)