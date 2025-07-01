from CarConnect.exceptions import AuthenticationException as CarConnectAuthenticationException
from CarConnect.exceptions import AdminNotFoundException as CarConnectAdminNotFoundException
from Dao import AdminService as CarConnectAdminService, CustomerService as CarConnectCustomerService

class AuthenticationService:
    def __init__(self):
        self.admin_service = CarConnectAdminService.AdminService()
        self.customer_service = CarConnectCustomerService.CustomerService()

    def authenticate_admin(self, username, password):
        try:
            admin = self.admin_service.get_admin_by_username(username)
            if admin.authenticate(password):
                return admin
            else:
                raise CarConnectAuthenticationException.AuthenticationException("Invalid password.")
        except CarConnectAdminNotFoundException.AdminNotFoundException as e:
            raise

    def authenticate_customer(self, username, password):
        try:
            customer = self.customer_service.get_customer_by_username(username)
            if customer is not None and customer.authenticate(password):
                return customer
            else:
                raise CarConnectAuthenticationException.AuthenticationException("Invalid username or password.")
        except CarConnectAuthenticationException.AuthenticationException as e:
            raise
