from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_login import LoginManager
network_host = 'mongodb+srv://softtodo:softtodo2020@cluster0-a1y5d.mongodb.net/softtodo?retryWrites=true&w=majority'


class Config(object):
    MONGODB_SETTINGS = {
        'db': 'softtodo',
        'host': 'mongodb+srv://softtodo:softtodo2020@cluster0-a1y5d.mongodb.net/softtodo?retryWrites=true&w=majority',
    }
    SECRET_KEY = 'hello world'


class FlaskApp(Flask):
    def __init__(self, import_name, config_object):
        super().__init__(import_name)
        self.config.from_object(config_object)
        self.session_mongoengine_interface = None
        self.session = None


app = FlaskApp(import_name=__name__, config_object='__init__.Config')
db = MongoEngine(app)
app.session_mongoengine_interface = MongoEngineSessionInterface(db)
login = LoginManager(app)
