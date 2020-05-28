from app import db

class Address(db.Document):
    code = db.StringField(unique=True, null=False, required=True)
    country = db.StringField(required=True)
    city = db.StringField()
    zip_code = db.IntField()

    def to_json(self):
        return {
            'code': self.code,
            'country': self.country,
            'city': self.city,
            'zip_code': self.zip_code
        }


class Customer(db.Document):
    code = db.StringField(unique=True, required=True)
    socialReason = db.StringField()
    revenueStamp = db.StringField()
    phones = db.ListField(db.StringField())
    emails = db.ListField(db.StringField(unique=True))
    address = db.ListField(db.ReferenceField(Address))
    password = db.StringField()
    login = db.StringField()

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
