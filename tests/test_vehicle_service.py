import unittest
from Dao import VehicleService as CarConnectVehicleService
from CarConnect.entity import Vehicle as CarConnectVehicle

class TestVehicleService(unittest.TestCase):
    def setUp(self):
        self.vehicle_service = CarConnectVehicleService.VehicleService()

    def test_add_new_vehicle(self):
        vehicle = CarConnectVehicle.Vehicle(
            model='TestModel',
            make='TestMake',
            year=2024,
            color='Green',
            registration_number='TEST9876',
            availability=True,
            daily_rate=1800.00,
            category='TestCategory'
        )
        result = self.vehicle_service.add_vehicle(vehicle)
        self.assertTrue(result)

    def test_update_vehicle_details(self):
        vehicle_id = 13
        new_rate = 2500.00
        result = self.vehicle_service.update_vehicle(vehicle_id, new_rate)
        self.assertTrue(result)

    def test_get_available_vehicles(self):
        vehicles = self.vehicle_service.get_available_vehicles()
        self.assertIsInstance(vehicles, list)
        self.assertGreaterEqual(len(vehicles), 0)

    def test_get_all_vehicles(self):
        vehicles = self.vehicle_service.get_all_vehicles()
        self.assertIsInstance(vehicles, list)
        self.assertGreaterEqual(len(vehicles), 0)

if __name__ == '__main__':
    unittest.main()
