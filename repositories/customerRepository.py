from models import Customer
from models import Address
from app import user_data_store
from flask_security.utils import hash_password


class AddressRepository(object):
    def __init__(self):
        super().__init__()
        self.address_class = Address

    def get_address_by_code(self, value): return self.address_class.objects.get(code=value)

    def get_address(self, param):
        return self.address_class.objects.filter(**param).first()

    def add_address(self, data):
        address = Address(**data)
        address.save()
        return address


class CustomerRepository(object):

    def __init__(self):
        super().__init__()
        self.user_data = user_data_store

    @staticmethod
    def get_customers(): return Customer.objects.all()

    def get_customer_by_login(self, data): return self.user_data.get_user(data.get('email'))

    @staticmethod
    def get_customer(code): return Customer.objects.get(code=code)

    def add_customer(self, data):
        data['password'] = hash_password(data.get('password'))
        customer = Customer(**data)
        customer.save()
        return customer

    @staticmethod
    def delete_customer(customer):
        try:
            customer.delete()
            return True
        except Exception as exception:
            raise exception
