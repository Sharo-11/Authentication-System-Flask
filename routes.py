from flask import Flask, render_template, url_for

def setup_routes(app: Flask):
    @app.route('/')
    def home():
        return render_template("home.html")
    
    @app.route("/login", methods = ['GET', 'POST'])
    def login():
        return render_template("login.html")
    
    @app.route("/register", methods = ['GET', 'POST'])
    def register():
        return render_template("register.html")

    @app.route("/register/student", methods = ['GET', 'POST'])
    def register_student():
        return render_template("register_student.html")
    
    @app.route("/register/company", methods = ['GET', 'POST'])
    def register_company():
        return render_template("register_company.html")