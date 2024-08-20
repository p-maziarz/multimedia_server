from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config') 

db = SQLAlchemy(app)

# Import routes or models
from app import routes, models
