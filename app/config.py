from secrets import token_hex
from json import loads


password_hash = None

with open('app/password.json', 'r') as f:
    password_hash = loads(f.read())

class Config(object):
    MONGODB_SETTINGS = {
        'db': 'softtodo',
        'host': 'localhost',
        'username': 'softtodo',
        'password': 'softtodo'
    }
    DEBUG = True
    SECRET_KEY = password_hash['SECRET_KEY']
    JWT_SECRET_KEY = password_hash['JWT_SECRET_KEY']
    SECURITY_PASSWORD_SALT = password_hash['SECURITY_PASSWORD_SALT']
    WTF_CSRF_SECRET_KEY = token_hex(64)
    WTF_CSRF_ENABLED = False
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
