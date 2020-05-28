from mongoengine import StringField, IntField, Document, ListField, ReferenceField
from flask_login import UserMixin

class Address(Document):
    code = StringField(primary_key=True)
    country = StringField(required=True)
    city = StringField()
    zip_code = StringField()

    def to_json(self):
        return {
            'code': self.code,
            'country': self.country,
            'city': self.city,
            'zip_code': self.zip_code
        }


class Customer(Document, UserMixin):
    code = StringField(primary_key=True)
    socialReason = StringField()
    revenueStamp = StringField()
    phones = ListField(StringField())
    emails = ListField(StringField(unique=True))
    address = ListField(ReferenceField(Address))
    password = StringField()
    login = StringField()

    def __init__(self, code, socialReason, revenueStamp, phones, emails, address, password, login):
        super().__init__()
        self.code = code
        self.socialReason = socialReason
        self.revenueStamp = revenueStamp
        self.phones = phones
        self.emails = emails
        self.address = address
        self.password = password
        self.login = login


    def to_json(self):
        addresses = []
        for i in self.address:
            addresses.append(i.to_json())
        return {
            'code': self.code,
            'socialReason': self.socialReason,
            'phones': self.phones,
            'emails': self.emails,
            'address': addresses,
            'password': self.password,
            'login': self.login
        }
