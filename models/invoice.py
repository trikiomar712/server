import mongoengine as db
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

    def __init__(self, products, customer, code, totalHT, totalNetHT, totalTVA, totalTTC, isScanned, date_modified,
                 *args, **values):
        super().__init__(*args, **values)
        self.products = products
        self.customer = customer
        self.code = code
        self.totalHT = totalHT
        self.totalNetHT = totalNetHT
        self.totalTVA = totalTVA
        self.totalTTC = totalTTC
        self.isScanned = isScanned
        self.date_modified = date_modified

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
        }
