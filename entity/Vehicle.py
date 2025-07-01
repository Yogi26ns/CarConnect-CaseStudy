class Vehicle:
    def __init__(self, vehicle_id=None, model=None, make=None, year=None, color=None, registration_number=None, availability=True, daily_rate=None,category=None):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.__make = make
        self.__year = year
        self.__color = color
        self.__registration_number = registration_number
        self.__availability = availability
        self.__daily_rate = daily_rate
        self.__category = category

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_registration_number(self):
        return self.__registration_number

    def is_available(self):
        return self.__availability

    def get_daily_rate(self):
        return self.__daily_rate
    def get_category(self):
        return self.__category