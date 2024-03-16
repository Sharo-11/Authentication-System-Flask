from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FileField
from wtforms.validators import InputRequired, Length, ValidationError, Email

db = SQLAlchemy()

class Student(db.Model, UserMixin):
    st_id = db.Column(db.Integer, primary_key = True)
    st_username = db.Column(db.String(20), nullable = False, unique = True)
    st_password = db.Column(db.String(80), nullable = False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    st_bio = db.Column(db.String(500), nullable = False)
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

class RegisterStudent(FlaskForm):
    st_id = StringField("Student Id", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Student Id"})
    st_username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    st_password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Password"})
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Last Name"})
    st_bio = StringField("Bio", validators=[InputRequired(), Length(min=2, max=500)], render_kw={"placeholder": "Bio"})
    st_email = StringField('Email', validators=[InputRequired(), Email(), Length(min=2, max=100)], render_kw={"placeholder": "Email"})
    st_campus = StringField('Campus', validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Campus"})
    st_department = StringField('Department', validators=[InputRequired(), Length(min=2, max=100)], render_kw={"placeholder": "Department"})
    st_year = IntegerField('Year', validators=[InputRequired()], render_kw={"placeholder": "Year"})
    st_profile_pic = FileField('Profile Picture', render_kw={"accept": "image/*"})
    st_submit = SubmitField("Register as Student")

    def validate_user_st(self, st_username):
        existing_user_st = Company.query.filter_by(st_username = st_username.data).first()

        if existing_user_sy:
            raise ValidationError("The username already exist. Please choose a different one.")

class RegisterCompany(FlaskForm):
    cp_id = StringField("Company Id", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Company Id"})
    cp_username = StringField("Username", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    cp_password = PasswordField("Password", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Password"})
    cp_name = StringField("Company Name", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Company Name"})
    cp_desc = StringField("Description", validators=[InputRequired(), Length(min=2, max=500)], render_kw={"placeholder": "Description"})
    cp_industry = StringField("Industry", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Industry"})
    cp_website = StringField("Website URL", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Website URL"})
    cp_email = StringField("Email", validators=[InputRequired(), Email(), Length(min=2, max=60)], render_kw={"placeholder": "Email"})
    cp_contact = IntegerField("Contact number", validators=[InputRequired()], render_kw={"placeholder": "Contact number"})
    cp_primary_contact = IntegerField("Primary Contact number", validators=[InputRequired()], render_kw={"placeholder": "Primary Contact number"})
    cp_size = StringField("Company Size", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Company Size"})
    cp_campus = StringField("Campus", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Campus"})
    cp_logo = FileField("Company Logo", validators=[InputRequired()], render_kw={"accept": "image/*"})
    cp_submit = SubmitField("Register as Company")


    def validate_user_cp(self, cp_username):
        existing_user_cp = Company.query.filter_by(cp_username = cp_username.data).first()

        if existing_user_cp:
            raise ValidationError("The username already exist. Please choose a different one.")

class LoginStudent(FlaskForm):
    st_username = StringField('Username', validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    st_password = PasswordField('Password', validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Password"})
    st_submit = SubmitField("Login as Student")

class LoginCompany(FlaskForm):
    cp_username = StringField("Username", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    cp_password = PasswordField("Password", validators=[InputRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Password"})
    cp_submit = SubmitField("Login as Company")
