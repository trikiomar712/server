from mongoengine import Document, StringField, FloatField, IntField, ReferenceField


class Product(Document):
    code = StringField(primary_key=True)
    description = StringField()
    realStock = IntField()
    initialStock = FloatField()
    buyingPrice = FloatField()
    sellingPrice = FloatField()
    stockMin = FloatField()
    stockMax = FloatField()
    discount = FloatField()
    quantitySold = IntField()

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
