import mongoengine as db
from flask_security import UserMixin, RoleMixin


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __init__(self, name, description, *args, **values):
        super().__init__(*args, **values)
        self.name = name
        self.description = description

    def to_json(self): return {'name': self.name, 'description': self.description}


class Address(db.Document):
    code = db.StringField(unique=True, required=True)
    country = db.StringField(required=True)
    cityOrVillage = db.StringField(required=True)
    zipCode = db.StringField(required=True)

    def __init__(self, code, country, cityOrVillage, zipCode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code
        self.country = country
        self.cityOrVillage = cityOrVillage
        self.zipCode = zipCode

    def to_json(self):
        return {
            'code': self.code,
            'country': self.country,
            'cityOrVillage': self.cityOrVillage,
            'zipCode': self.zipCode
        }


class Customer(db.Document, UserMixin):
    code = db.StringField(unique=True, required=True)
    socialReason = db.StringField(unique=True, required=True)
    revenueStamp = db.StringField()
    phones = db.ListField(db.StringField(unique=True), default=[])
    emails = db.ListField(db.StringField(unique=True), default=[])
    address = db.ListField(db.ReferenceField(Address), default=[])
    password = db.StringField(required=True)
    login = db.StringField(required=True, unique=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])
    active = db.BooleanField(default=False)

    def __init__(self, code, socialReason, revenueStamp, password, login, phones=None, emails=None, address=None,
                 roles=None, active=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if address is None:
            address = []
        if emails is None:
            emails = []
        if phones is None:
            phones = []
        if roles is None:
            roles = []
        self.code = code
        self.socialReason = socialReason
        self.revenueStamp = revenueStamp
        self.phones = phones
        self.emails = emails
        self.address = address
        self.password = password
        self.login = login
        self.roles = roles
        self.active = active

    def to_json(self):
        addresses = []
        roles = []
        for i, j in zip(self.address, self.roles):
            addresses.append(i.to_json())
            roles.append(j.to_json)
        return {
            'code': self.code,
            'socialReason': self.socialReason,
            'phones': self.phones,
            'emails': self.emails,
            'address': addresses,
            'login': self.login,
            'password': self.password,
            'revenueStamp': self.revenueStamp,
            'roles': roles
        }
