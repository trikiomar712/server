from app import db
from .product import Product


class InvoiceLine(db.Document):
    code = db.ReferenceField(Product)
