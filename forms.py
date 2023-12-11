from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, DataRequired, Email, ValidationError

class StudentRegistrationForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "First Name"})
    last_name = StringField(validators=[InputRequired(), Length(min=2, max=50)], render_kw={"placeholder": "Last Name"})
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    skills = StringField(validators=[Length(min=2, max=50)], render_kw={"placeholder": "Skills"})
    dept = StringField(validators=[Length(min=2, max=150)], render_kw={"placeholder": "Department"})
    campus_st = StringField(validators=[Length(min=5, max=300)], render_kw={"placeholder": "Campus"})
    profile_pic = FileField('Profile Picture', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField("Register")

    def validate_username(self, username):  # Changed from validate_user_cp
        existing_user_name = StudentRegistrationForm.query.filter_by(username=self.username.data).first()
        if existing_user_name:
            raise ValidationError("Username Already Exists! Please choose a different one.")

class CompanyRegistrationForm(FlaskForm):
    company_name = StringField(validators=[InputRequired(), Length(min=2, max=200)], render_kw={"placeholder": "Company Name"})
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    desc = StringField(validators=[InputRequired(), Length(min=2, max=500)], render_kw={"placeholder": "Description"})
    industry = StringField(validators=[InputRequired(), Length(min=2, max=250)], render_kw={"placeholder": "Industry"})
    campus_cp = StringField(validators=[InputRequired(), Length(min=5, max=300)], render_kw={"placeholder": "Campus"})
    website_url = StringField(validators=[Length(max=500)], render_kw={"placeholder": "Website URL"})
    email_cp = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    company_size_min = StringField(validators=[Length(min=1, max=10)], render_kw={"placeholder": "Company Size Min"})
    company_size_max = StringField(validators=[Length(min=1, max=10)], render_kw={"placeholder": "Company Size Max"})
    company_logo = FileField('Company Logo', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField("Register")

    def validate_username(self, username):  # Changed from validate_user_st
        existing_user_name = CompanyRegistrationForm.query.filter_by(username=self.username.data).first()
        if existing_user_name:
            raise ValidationError("Username Already Exists! Please choose a different one.")