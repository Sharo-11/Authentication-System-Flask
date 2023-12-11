from flask import render_template
from app import app
from forms import StudentRegistrationForm, CompanyRegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerasst')
def registerasst():
    form = StudentRegistrationForm()
    return render_template('register_st.html', form=form)

@app.route('/registerascp')
def registerascp():
    form = CompanyRegistrationForm()
    return render_template('register_cp.html', form=form)
