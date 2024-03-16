from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import setup_routes
from models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CareerOtaku17'

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Example URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration for upload folder
app.config['UPLOAD_FOLDER'] = './Upload'

# Initialize SQLAlchemy extension
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# Call for the routes
setup_routes(app)

if __name__ == '__main__':
    app.run(debug = True)