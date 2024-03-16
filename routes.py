from flask import render_template, url_for, request, redirect, Flask
import os
from werkzeug.utils import secure_filename
from models import *
from extensions import db, bcrypt

def setup_routes(app: Flask):
    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")
    
    @app.route("/login", methods=['GET', 'POST'])
    def login():
        return render_template("login.html")
    
    @app.route("/login/student", methods=['GET', 'POST'])
    def login_student():
        form = LoginStudent()
        return render_template("login_student.html", form=form)
    
    @app.route("/login/company", methods=['GET', 'POST'])
    def login_company():
        form = LoginCompany()
        return render_template("login_company.html", form=form)

    @app.route("/register", methods=['GET', 'POST'])
    def register():
        return render_template("register.html")

    @app.route("/register/student", methods=['GET', 'POST'])
    def register_student():
        form = RegisterStudent()

        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.st_password.data).decode('utf-8')
            new_st = Student(
                st_username=form.st_username.data,
                st_password=hashed_password,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                st_bio=form.st_bio.data,
                st_email=form.st_email.data,
                st_campus=form.st_campus.data,
                st_department=form.st_department.data,
                st_year=form.st_year.data,
                st_profile_pic=''  # You may need to handle profile pic upload separately
            )
            db.session.add(new_st)
            db.session.commit()
            
            print("Form validated successfully!")
            return redirect(url_for('login_student'))  # Redirect to login page after successful registration

        else:
            print("Form validation failed. Errors:", form.errors)
        return render_template("register_student.html", form=form)

    
    @app.route("/register/company", methods=['GET', 'POST'])
    def register_company():
        form = RegisterCompany()

        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.cp_password.data).decode('utf-8')
            new_company = Company(
                cp_username=form.cp_username.data,
                cp_password=hashed_password,
                cp_name=form.cp_name.data,
                cp_desc=form.cp_desc.data,
                cp_industry=form.cp_industry.data,
                cp_website=form.cp_website.data,
                cp_email=form.cp_email.data,
                cp_contact=form.cp_contact.data,
                cp_primary_contact=form.cp_primary_contact.data,
                cp_size=form.cp_size.data,
                cp_campus=form.cp_campus.data,
                cp_logo=form.cp_logo.data 
            )
            db.session.add(new_company)
            db.session.commit()
            print("Form validated successfully!")
            return redirect(url_for('login_company'))

        else:
            print("Form validation failed. Errors:", form.errors)
        return render_template("register_student.html", form=form)

        return render_template("register_company.html", form=form)


    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return 'File uploaded successfully'
