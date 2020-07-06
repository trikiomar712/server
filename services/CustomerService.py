from repositories import CustomerRepository, AddressRepository


class CustomerService(object):
    def __init__(self):
        super().__init__()
        self.customer = None
        self.customerRepository = CustomerRepository()
        self.addressRepository = AddressRepository()

    def get_customers(self): return self.customerRepository.get_customers()

    def get_specific_customer(self, data):
        print(data)
        self.customer = self.customerRepository.get_customer_by_login(data)
        print(self.customer.password)
        return self.customer.to_json()

    def add_customer(self, data):
        if data.get('cin') is None:
            raise Exception('customer must have cin')
        elif data.get('socialReason') is None:
            raise Exception('customer must have social reason')
        elif data.get('revenueStamp') is None:
            raise Exception('customer must have revenue stamp')
        elif data.get('phones') is None or data.get('phones') == []:
            raise Exception('customer must have at least one phone number')
        elif data.get('address') is None or data.get('address') == []:
            raise Exception('customer must have address')
        else:
            addresses = []
            for i in data.get('address'):
                address = self.addressRepository.get_address(i)
                if address is None:
                    address = self.addressRepository.add_address(i)
                else:
                    address = address.id
                addresses.append(address)
            data['address'] = addresses
            self.customer = self.customerRepository.add_customer(data)
            return self.customer.to_json()

    def delete_customer(self, data):
        customer = self.customerRepository.get_customer(code=data)
        if customer is not None:
            customer.delete()
            return True
        else:
            return False

    def reset_password(self, data):
        self.customer.password = hash_password(data)
        self.customer.save()
        return self.customer.to_json()
