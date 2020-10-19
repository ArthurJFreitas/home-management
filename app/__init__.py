from flask import Flask
from flask import request


from services.database import db

def create_app(config_object=ProdConfig):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)

from app.controllers.users import users
from app.controllers.homes import homes


app = Flask(__name__)

