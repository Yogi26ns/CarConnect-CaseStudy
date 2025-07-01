class ReservationNotFoundException(Exception):
    def __init__(self, message="Reservation not found"):
        super().__init__(message)