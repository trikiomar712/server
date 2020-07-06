from flask import Flask
from flask_wtf import CSRFProtect
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, login_required
from models import Customer, Role


class FlaskApp(Flask):
    def __init__(self, import_name):
        super().__init__(import_name=import_name)
        CORS(app=self)
        self.csrf = CSRFProtect(self)
        self.config.from_object('app.config.Config')
        self.mongo_engine = MongoEngine(self)
        self.jwt_manager = JWTManager(self)
        self.user_data_store = MongoEngineUserDatastore(self.mongo_engine, Customer, Role)
        self.security = Security(self, datastore=self.user_data_store)


app = FlaskApp(import_name=__name__)
user_data_store = app.user_data_store
security = app.security
csrf = app.csrf
