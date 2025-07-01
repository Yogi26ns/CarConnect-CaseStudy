from abc import ABC, abstractmethod

class ICustomerService(ABC):
    @abstractmethod
    def register_customer(self, customer):
        pass

    @abstractmethod
    def get_customer_by_username(self, username):
        pass

    @abstractmethod
    def authenticate_customer(self, username, password):
        pass

    @abstractmethod
    def update_customer_profile(self, customer_id, field, new_value):
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass
