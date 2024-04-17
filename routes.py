from flask import render_template, url_for, request, redirect, Flask, flash, session
import os
from flask_login import UserMixin, login_required, login_user, LoginManager, logout_user, current_user
from werkzeug.utils import secure_filename
from models import *
from extensions import *

def setup_routes(app: Flask):
    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route("/login", methods=['GET', 'POST'])
    def login():
        return render_template("login.html")

    @login_manager.user_loader
    def load_user(user_id):
        if user_id.startswith('st_'):
            # Remove prefix and fetch student
            student_id = user_id[3:]  # Removes the first 3 characters 'st_'
            return Student.query.get(int(student_id))
        elif user_id.startswith('cp_'):
            # Remove prefix and fetch company
            company_id = user_id[3:]  # Removes the first 3 characters 'cp_'
            return Company.query.get(int(company_id))
        return None


    @app.route("/login/student", methods=['GET', 'POST'])
    def login_student():
        form = LoginStudent()
        if form.validate_on_submit():
            student = Student.query.filter_by(st_username=form.st_username.data).first()
            if student and bcrypt.check_password_hash(student.st_password, form.st_password.data):
                login_user(student)
                session['user_type'] = 'student'
                return redirect(url_for("dashboard"))
            flash('Invalid username or password')
        return render_template("login_student.html", form=form)

    @app.route("/login/company", methods=['GET', 'POST'])
    def login_company():
        form = LoginCompany()
        if form.validate_on_submit():
            company = Company.query.filter_by(cp_username=form.cp_username.data).first()
            if company and bcrypt.check_password_hash(company.cp_password, form.cp_password.data):
                login_user(company)
                session['user_type'] = 'company'
                return redirect(url_for("dashboard"))
            flash('Invalid username or password')
        return render_template("login_company.html", form=form)

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return redirect("http://127.0.0.1:5001/student")

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
                st_profile_pic=''  # Handle profile pic upload separately
            )
            db.session.add(new_st)
            db.session.commit()
            return redirect(url_for('login_student'))
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
                cp_logo=''  # Handle logo upload separately
            )
            db.session.add(new_company)
            db.session.commit()
            return redirect(url_for('login_company'))
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
