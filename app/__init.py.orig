from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap




bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    #initializing the application
    app = Flask(__name__)

    #Initializing Flask Extenstion
    bootstrap.init_app(app)
    db.init_app(app)