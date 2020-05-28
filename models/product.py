from app import db


class Product(db.Document):
    code = db.StringField(primary_key=True)
    description = db.StringField()
    realStock = db.IntField()
    initialStock = db.FloatField()
    buyingPrice = db.FloatField()
    sellingPrice = db.FloatField()
    stockMin = db.FloatField()
    stockMax = db.FloatField()
    discount = db.FloatField()
    quantitySold = db.IntegerField()

    def to_json(self):
        return {
            'code': self.code,
            'description': self.description,
            'realStock': self.realStock,
            'initialStock': self.initialStock,
            'buyingPrice': self.buyingPrice,
            'sellingPrice': self.sellingPrice,
            'stockMin': self.stockMin,
            'stockMax': self.stockMax,
            'discount': self.discount,
            'quantityStock': self.quantitySold
        }
