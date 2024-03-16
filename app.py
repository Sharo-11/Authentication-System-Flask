from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import setup_routes
from models import *

app = Flask(__name__)

# Call for the routes
setup_routes(app)

db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "CarrerOtaku17"

db.create_all()

if __name__ == '__main__':
    app.run(debug = True)