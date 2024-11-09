from flask import Flask
from flask_migrate import Migrate
from models import db

def create_app():
    app = Flask(__name__)
    ....
    
    migrate = Migrate(app, db)  # Инициализация миграции

    return app
