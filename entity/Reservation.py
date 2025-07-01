class Reservation:
    def __init__(self, reservation_id=None, customer_id=None, vehicle_id=None, start_date=None, end_date=None, total_cost=None,status=None):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__vehicle_id = vehicle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__total_cost = total_cost
        self.__status = status
    def get_reservation_id(self):
        return self.__reservation_id

    def get_customer_id(self):
        return self.__customer_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_total_cost(self):
        return self.__total_cost

    def get_status(self):
        return self.__status