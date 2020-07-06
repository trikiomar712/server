from Controllers import CustomerView
from app import app

customer_view = CustomerView().as_view('customerView')
app.add_url_rule('/log_in', view_func=customer_view, methods=['POST'])
app.add_url_rule('/signUp', view_func=customer_view, methods=['POST'])
app.add_url_rule('/logout', view_func=customer_view, methods=['POST'])
app.add_url_rule('/reset_password', view_func=customer_view, methods=['POST'])
if __name__ == '__main__':
    app.run()
