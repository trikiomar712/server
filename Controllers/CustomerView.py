from flask.views import MethodView
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from services.CustomerService import CustomerService


class CustomerView(MethodView):
    def __init__(self):
        super().__init__()
        self.customer = None
        self.customerService = CustomerService()

    def get(self):
        return jsonify(self.customerService.get_customers())

    def post(self):
        if request.json['request'] == 'login':
            return self.login(request.json.get('user', None))
        elif request.json['request'] == 'sign_up':
            return self.customerService.add_customer(request.json.get('user')).to_json()
        elif request.json['request'] == 'reset_password':
            return self.reset_password(request.json.get('password'))
        elif request.json['request'] == 'logout':
            return self.logout(request.json.get('code'))

    def login(self, data):
        self.customer = self.customerService.get_specific_customer(data)
        if self.customer is None:
            raise Exception('customer not found check if the user exists')
        else:
            return jsonify({
                'access': create_access_token(self.customer.login, fresh=True),
                'refresh': create_refresh_token(self.customer.login),
            })

    def reset_password(self, data):
        try:
            self.customer.password = data
            self.customer.save()
            return jsonify({'password changed': True})
        except Exception as exception:
            raise exception

