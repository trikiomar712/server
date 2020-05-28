from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import UserMixin
network_host = 'mongodb+srv://softtodo:softtodo2020@cluster0-a1y5d.mongodb.net/softtodo?retryWrites=true&w=majority'


class Config(object):
    MONGODB_SETTINGS = {
        'db': 'softtodo',
        'host': 'localhost',
        'username': 'softtodo',
        'password': 'softtodo2020'
    }
    SECRET_KEY = 'hello world'


class FlaskApp(Flask):
    def __init__(self, import_name, config_object):
        super().__init__(import_name)
        self.config.from_object(config_object)
        self.session = None


app = FlaskApp(import_name=__name__, config_object='__init__.Config')
db = MongoEngine(app)
