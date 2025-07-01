from abc import ABC, abstractmethod

class IReservationService(ABC):
    @abstractmethod
    def create_reservation(self, reservation):
        pass

    @abstractmethod
    def get_customer_reservations(self, customer_id):
        pass

    @abstractmethod
    def is_vehicle_available(self, vehicle_id, start_date, end_date):
        pass

    @abstractmethod
    def update_reservation(self, reservation_id, new_vehicle_id, new_start_date, new_end_date):
        pass
