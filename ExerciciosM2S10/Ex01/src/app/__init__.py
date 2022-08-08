import os

from flask import Flask
from flask_migrate import Migrate

from src.app.db import DB, MA
from src.app.config import app_config

def create_app():

    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv('FLASK_ENV')])

    DB.init_app(app)
    MA.init_app(app)

    Migrate(app=app, db=DB, directory="./src/app/migrations")

    return app

