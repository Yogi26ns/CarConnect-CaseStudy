import unittest
from Dao import CustomerService as CarConnectCustomerService
from Dao import VehicleService as CarConnectVehicleService
from Dao import AdminService as CarConnectAdminService

class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.customer_service = CarConnectCustomerService.CustomerService()
        self.vehicle_service = CarConnectVehicleService.VehicleService()
        self.admin_service = CarConnectAdminService.AdminService()

    def test_customer_authentication_invalid(self):
        with self.assertRaises(Exception):
            self.customer_service.authenticate_customer('invalid_user', 'wrong_password')

    def test_update_customer_information(self):
        update_result = self.customer_service.update_customer_profile(2, 'FirstName', 'TestName')
        self.assertTrue(update_result)

    def test_get_available_vehicles(self):
        available_vehicles = self.vehicle_service.get_available_vehicles()
        self.assertIsInstance(available_vehicles, list)
        self.assertGreaterEqual(len(available_vehicles), 0)

    def test_get_all_vehicles(self):
        all_vehicles = self.vehicle_service.get_all_vehicles()
        self.assertIsInstance(all_vehicles, list)
        self.assertGreaterEqual(len(all_vehicles), 0)

if __name__ == '__main__':
    unittest.main()
