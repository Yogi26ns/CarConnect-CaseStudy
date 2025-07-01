from abc import ABC, abstractmethod

class IVehicleService(ABC):
    @abstractmethod
    def add_vehicle(self, vehicle):
        pass

    @abstractmethod
    def get_all_vehicles(self):
        pass

    @abstractmethod
    def update_vehicle(self, vehicle_id, new_rate):
        pass

    @abstractmethod
    def delete_vehicle(self, vehicle_id):
        pass

    @abstractmethod
    def is_vehicle_active(self, vehicle_id):
        pass

    @abstractmethod
    def get_vehicle_daily_rate(self, vehicle_id):
        pass

    @abstractmethod
    def mark_vehicle_unavailable(self, vehicle_id):
        pass

    @abstractmethod
    def get_available_vehicles(self):
        pass
