from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, Student, Company

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisakey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

# Add the following for debugging
print("Flask app created")

@app.route('/')
def home():
    # Add the following for debugging
    print("Home route accessed")
    return render_template('home.html')

@app.route('/login')
def login():
    # Add the following for debugging
    print("Login route accessed")
    return render_template('login.html')

@app.route('/register')
def register():
    # Add the following for debugging
    print("Register route accessed")
    return render_template('register.html')

if __name__ == '__main__':
    # Add the following for debugging
    print("App is running")
    app.run(debug=True)
