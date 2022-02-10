from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError

# create app
app = Flask(__name__)

# create database connection
db = SQLAlchemy(app)

# migrating app

migrate  = Migrate(app, db)

# configuration file
if(app.config["ENV"] == "production"):
    app.config.from_object("config.ProductionConfig")

elif(app.config["ENV"] == "development"):
    app.config.from_object("config.DevelopmentConfig")

else:
    app.config.from_object("config.TestingConfig")

from app import views
from app import admin_views
from app.Users.Authentication import signup
from app.models import Authentication