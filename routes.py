from flask import Flask, render_template, url_for, request
import os
from werkzeug.utils import secure_filename
from models import LoginStudent, LoginCompany, RegisterCompany, RegisterStudent

def setup_routes(app: Flask):
    @app.route('/')
    def home():
        return render_template("home.html")
    
    @app.route("/login", methods = ['GET', 'POST'])
    def login():
        return render_template("login.html")
    
    @app.route("/login/student", methods = ['GET', 'POST'])
    def login_student():
        form = LoginStudent()
        return render_template("login_student.html", form = form)
    
    @app.route("/login/company", methods = ['GET', 'POST'])
    def login_company():
        form = LoginCompany()
        return render_template("login_company.html", form = form)

    @app.route("/register", methods = ['GET', 'POST'])
    def register():
        return render_template("register.html")

    @app.route("/register/student", methods = ['GET', 'POST'])
    def register_student():
        form = RegisterStudent()
        return render_template("register_student.html", form = form)
    
    @app.route("/register/company", methods = ['GET', 'POST'])
    def register_company():
        form = RegisterCompany()
        return render_template("register_company.html", form = form)

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
