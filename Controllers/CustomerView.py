from flask.views import MethodView
from flask import request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from services.CustomerService import CustomerService
from flask_security import logout_user

class CustomerView(MethodView):
    def __init__(self):
        super().__init__()
        self.customer = None
        self.customerService = CustomerService()

    def get(self):
        return jsonify(self.customerService.get_customers())

    def post(self):
        if request.json.get('request') is None:
            raise Exception('you have to specify the request')
        if request.json['request'] == 'login':
            return self.login(request.json.get('user'))
        elif request.json['request'] == 'signup':
            if request.json.get('user') is None:
                raise Exception('give us the user')
            return jsonify(self.customerService.add_customer(request.json.get('user')))
        elif request.json['request'] == 'reset_password':
            return self.reset_password(request.json.get('password'))
        elif request.json['request'] == 'logout':
            return self.logout(request.json.get('code'))

    def login(self, data):
        print(data)
        self.customer = self.customerService.get_specific_customer(data)
        if self.customer is None:
            raise Exception('customer not found check if the user exists')
        else:
            return jsonify({
                'refresh': create_access_token(self.customer['email'], fresh=True),
                'access': create_refresh_token(self.customer),
            })

    def reset_password(self, data):
        try:
            self.customer.password = data
            self.customer.save()
            return jsonify({'password changed': True})
        except Exception as exception:
            raise exception

    def logout(self):
        try:
            logout_user()
            return jsonify({"logout": True})
        except Exception as exception:
            return jsonify({"exception": 'exception'}), 400
