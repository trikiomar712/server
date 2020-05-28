from app import db
from .product import Product
from .customer import Customer
import datetime


class Invoice(db.Document):
    products = db.ListField(db.ReferenceField(Product))
    customer = db.ReferenceField(Customer)
    code = db.StringField(unique=True, null=False)
    totalHT = db.FloatField()
    totalNetHT = db.FloatField()
    totalTVA = db.FloatField()
    totalTTC = db.FloatField()
    isScanned = db.BooleanField()
    date_modified = db.DateTimeField(default=datetime.datetime.utcnow)

    def to_json(self):
        products = self.products
        products_to_json = []
        for i in products:
            products_to_json.append(i.to_json())
        return {
            'code': self.code,
            'products': products_to_json,
            'customer': self.customer.to_json(),
            'total_ht': self.totalHT,
            'totalNetHT': self.totalNetHT,
            'totalTVA': self.totalTVA,
            'totalTTC': self.totalTTC,
            'isScanned': self.is_scanned
        }
