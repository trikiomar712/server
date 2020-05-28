from mongoengine import StringField, IntField, Document, ListField, ReferenceField

class Address(Document):
    code = StringField(unique=True, null=False, required=True)
    country = StringField(required=True)
    city = StringField()
    zip_code = IntField()

    def to_json(self):
        return {
            'code': self.code,
            'country': self.country,
            'city': self.city,
            'zip_code': self.zip_code
        }


class Customer(Document):
    code = StringField(unique=True, required=True)
    socialReason = StringField()
    revenueStamp = StringField()
    phones = ListField(StringField())
    emails = ListField(StringField(unique=True))
    address = ListField(ReferenceField(Address))
    password = StringField()
    login = StringField()

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
