from flask import Flask
from extensions import db, bcrypt, login_manager
from routes import setup_routes
from models import Student, Company
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CareerOtaku17'

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration for upload folder
app.config['UPLOAD_FOLDER'] = './Uploads'

# Initialize SQLAlchemy extension
db.init_app(app)

# Initialize Flask Login
login_manager.init_app(app)
login_manager.login_view = "login"

# Initialize Bcrypt extension
bcrypt.init_app(app)

# Call for the routes
setup_routes(app)

# Create all database tables
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
