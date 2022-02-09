from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create app
app = Flask(__name__)

# create database connection
db = SQLAlchemy(app)

from app import views
from app import admin_views
from app.Users.Authentication import signup