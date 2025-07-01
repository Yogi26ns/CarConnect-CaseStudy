# from datetime import datetime
# import mysql.connector
# from util.DBPropertyUtil import DBPropertyUtil
# from util.DBConnUtil import DBConnUtil
# from CarConnect.entity import Reservation as CarConnectReservation
# from CarConnect.Dao import IReservationService as CarConnectIReservation
# from CarConnect.exceptions import ReservationNotFoundException as CarConnectReservationNotFoundException
# from CarConnect.Dao.VehicleService import VehicleService
#
# class ReservationService(CarConnectIReservation.IReservationService):
#     def create_reservation(self, reservation):
#         conn=None
#         cursor=None
#         try:
#             connection_properties = DBPropertyUtil.get_connection_properties()
#             conn = DBConnUtil.get_connection(connection_properties)
#             cursor = conn.cursor()
#
#             query = '''
#                 INSERT INTO reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost,Status)
#                 VALUES (%s, %s, %s, %s, %s, %s)
#             '''
#             values = (
#                 reservation.get_customer_id(),
#                 reservation.get_vehicle_id(),
#                 reservation.get_start_date(),
#                 reservation.get_end_date(),
#                 reservation.get_total_cost(),
#                 'Confirmed'
#             )
#
#             cursor.execute(query, values)
#             conn.commit()
#
#             print("\nReservation created successfully!")
#
#         except mysql.connector.Error as e:
#             print(f"Database Error: {e}")
#         finally:
#             if conn.is_connected():
#                 cursor.close()
#                 DBConnUtil.close_connection(conn)
#
#     def get_customer_reservations(self, customer_id):
#         conn = None
#         cursor = None
#         reservations = []
#         try:
#             connection_properties = DBPropertyUtil.get_connection_properties()
#             conn = DBConnUtil.get_connection(connection_properties)
#             cursor = conn.cursor()
#
#             query = "SELECT * FROM reservation WHERE CustomerID = %s"
#             cursor.execute(query, (customer_id,))
#             results = cursor.fetchall()
#
#             if not results:
#                 raise CarConnectReservationNotFoundException.ReservationNotFoundException("No reservations found for this customer.")
#
#             for result in results:
#                 reservation = CarConnectReservation.Reservation(
#                     reservation_id=result[0],
#                     customer_id=result[1],
#                     vehicle_id=result[2],
#                     start_date=result[3],
#                     end_date=result[4],
#                     total_cost=result[5]
#                 )
#                 reservations.append(reservation)
#
#             return reservations
#
#         except mysql.connector.Error as e:
#             print(f"Database Error: {e}")
#         finally:
#             if conn.is_connected():
#                 cursor.close()
#                 DBConnUtil.close_connection(conn)
#
#     def is_vehicle_available(self, vehicle_id, start_date, end_date):
#         conn = None
#         cursor = None
#         try:
#             connection_properties = DBPropertyUtil.get_connection_properties()
#             conn = DBConnUtil.get_connection(connection_properties)
#             cursor = conn.cursor()
#
#             query = "SELECT * FROM reservation WHERE VehicleID = %s AND (StartDate <= %s AND EndDate >= %s)"
#             cursor.execute(query, (vehicle_id, end_date, start_date))
#             result = cursor.fetchone()
#
#             if result:
#                 return False
#             else:
#                 return True
#
#         except mysql.connector.Error as e:
#             print(f"Database Error: {e}")
#             return False
#         finally:
#             if cursor is not None:
#                 cursor.close()
#             if conn is not None and conn.is_connected():
#                 DBConnUtil.close_connection(conn)
#
#     def get_reservation_by_id(self, reservation_id):
#         conn = None
#         cursor = None
#         try:
#             connection_properties = DBPropertyUtil.get_connection_properties()
#             conn = DBConnUtil.get_connection(connection_properties)
#             cursor = conn.cursor()
#
#             query = "SELECT * FROM reservation WHERE ReservationID = %s"
#             cursor.execute(query, (reservation_id,))
#             result = cursor.fetchone()
#
#             if result:
#                 reservation = CarConnectReservation.Reservation(
#                     reservation_id=result[0],
#                     customer_id=result[1],
#                     vehicle_id=result[2],
#                     start_date=result[3],
#                     end_date=result[4],
#                     total_cost=result[5],
#                     status=result[6]
#                 )
#                 return reservation
#             else:
#                 return None
#
#         except mysql.connector.Error as e:
#             print(f"Database Error: {e}")
#             return None
#         finally:
#             if conn.is_connected():
#                 cursor.close()
#                 DBConnUtil.close_connection(conn)
#
#     def cancel_reservation(self, reservation_id):
#         conn = None
#         cursor = None
#         try:
#             connection_properties = DBPropertyUtil.get_connection_properties()
#             conn = DBConnUtil.get_connection(connection_properties)
#             cursor = conn.cursor()
#
#             # Set status to cancelled
#             query = "UPDATE reservation SET Status = 'Cancelled' WHERE ReservationID = %s"
#             cursor.execute(query, (reservation_id,))
#             conn.commit()
#
#             if cursor.rowcount > 0:
#                 # print("\nReservation cancelled successfully!")
#                 return True
#             else:
#                 print("\nReservation not found!")
#                 return False
#
#         except mysql.connector.Error as e:
#             print(f"Database Error: {e}")
#             return False
#         finally:
#             if conn.is_connected():
#                 cursor.close()
#                 DBConnUtil.close_connection(conn)
#
#     def update_reservation(self, reservation_id, new_vehicle_id, new_start_date, new_end_date):
#         conn = None
#         cursor = None
#         try:
#             # Check if the new vehicle is available for the new dates
#             if not self.is_vehicle_available(new_vehicle_id, new_start_date, new_end_date):
#                 print("\nThe selected vehicle is not available for the given dates.")
#                 return False
#
#             connection_properties = DBPropertyUtil.get_connection_properties()
#             conn = DBConnUtil.get_connection(connection_properties)
#             cursor = conn.cursor()
#
#             # Calculate new total cost
#
#             vehicle_service = VehicleService()
#             daily_rate = vehicle_service.get_vehicle_daily_rate(new_vehicle_id)
#             start = datetime.strptime(new_start_date, '%Y-%m-%d')
#             end = datetime.strptime(new_end_date, '%Y-%m-%d')
#             num_days = (end - start).days + 1
#             total_cost = num_days * daily_rate
#
#             # Update the reservation
#             query = "UPDATE reservation SET VehicleID = %s, StartDate = %s, EndDate = %s, TotalCost = %s WHERE ReservationID = %s"
#             cursor.execute(query, (new_vehicle_id, new_start_date, new_end_date, total_cost, reservation_id))
#             conn.commit()
#
#             if cursor.rowcount > 0:
#                 print(f"\nReservation updated successfully! New Total Cost: ₹{total_cost}")
#                 return True
#             else:
#                 print("\nReservation not found or update failed!")
#                 return False
#
#         except mysql.connector.Error as e:
#             print(f"Database Error: {e}")
#             return False
#         finally:
#             if conn.is_connected():
#                 cursor.close()
#                 DBConnUtil.close_connection(conn)

from datetime import datetime
import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil
from CarConnect.entity import Reservation as CarConnectReservation
from CarConnect.Dao import IReservationService as CarConnectIReservation
from CarConnect.exceptions import ReservationNotFoundException as CarConnectReservationNotFoundException
from CarConnect.Dao.VehicleService import VehicleService


class ReservationService(CarConnectIReservation.IReservationService):

    def create_reservation(self, reservation):
        conn = None
        cursor = None
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = '''
                INSERT INTO reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                VALUES (%s, %s, %s, %s, %s, %s)
            '''
            values = (
                reservation.get_customer_id(),
                reservation.get_vehicle_id(),
                reservation.get_start_date(),
                reservation.get_end_date(),
                reservation.get_total_cost(),
                'Confirmed'
            )

            cursor.execute(query, values)
            conn.commit()

            print("\nReservation created successfully!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

    def get_customer_reservations(self, customer_id):
        conn = None
        cursor = None
        reservations = []
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM reservation WHERE CustomerID = %s"
            cursor.execute(query, (customer_id,))
            results = cursor.fetchall()

            if not results:
                raise CarConnectReservationNotFoundException.ReservationNotFoundException("No reservations found for this customer.")

            for result in results:
                reservation = CarConnectReservation.Reservation(
                    reservation_id=result[0],
                    customer_id=result[1],
                    vehicle_id=result[2],
                    start_date=result[3],
                    end_date=result[4],
                    total_cost=result[5],
                    status=result[6]
                )
                reservations.append(reservation)

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

        return reservations

    def is_vehicle_available(self, vehicle_id, start_date, end_date):
        conn = None
        cursor = None
        is_available = False
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM reservation WHERE VehicleID = %s AND (StartDate <= %s AND EndDate >= %s)"
            cursor.execute(query, (vehicle_id, end_date, start_date))
            result = cursor.fetchone()

            is_available = result is None

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

        return is_available

    def get_reservation_by_id(self, reservation_id):
        conn = None
        cursor = None
        reservation = None
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM reservation WHERE ReservationID = %s"
            cursor.execute(query, (reservation_id,))
            result = cursor.fetchone()

            if result:
                reservation = CarConnectReservation.Reservation(
                    reservation_id=result[0],
                    customer_id=result[1],
                    vehicle_id=result[2],
                    start_date=result[3],
                    end_date=result[4],
                    total_cost=result[5],
                    status=result[6]
                )

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

        return reservation

    def cancel_reservation(self, reservation_id):
        conn = None
        cursor = None
        success = False
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "UPDATE reservation SET Status = 'Cancelled' WHERE ReservationID = %s"
            cursor.execute(query, (reservation_id,))
            conn.commit()

            if cursor.rowcount > 0:
                success = True
            else:
                print("\nReservation not found!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

        return success

    def update_reservation(self, reservation_id, new_vehicle_id, new_start_date, new_end_date):
        conn = None
        cursor = None
        success = False
        try:
            if not self.is_vehicle_available(new_vehicle_id, new_start_date, new_end_date):
                print("\nThe selected vehicle is not available for the given dates.")
                return False

            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            vehicle_service = VehicleService()
            daily_rate = vehicle_service.get_vehicle_daily_rate(new_vehicle_id)
            start = datetime.strptime(new_start_date, '%Y-%m-%d')
            end = datetime.strptime(new_end_date, '%Y-%m-%d')
            num_days = (end - start).days + 1
            total_cost = num_days * daily_rate

            query = "UPDATE reservation SET VehicleID = %s, StartDate = %s, EndDate = %s, TotalCost = %s WHERE ReservationID = %s"
            cursor.execute(query, (new_vehicle_id, new_start_date, new_end_date, total_cost, reservation_id))
            conn.commit()

            if cursor.rowcount > 0:
                print(f"\nNew Total Cost: ₹{total_cost}")
                success = True
            else:
                print("\nReservation not found or update failed!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

        return success

    def get_all_reservations(self):
        reservations = []
        conn = None
        cursor = None
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM reservation"
            cursor.execute(query)
            results = cursor.fetchall()

            for result in results:
                reservation = CarConnectReservation.Reservation(
                    reservation_id=result[0],
                    customer_id=result[1],
                    vehicle_id=result[2],
                    start_date=result[3],
                    end_date=result[4],
                    total_cost=result[5],
                    status=result[6]
                )
                reservations.append(reservation)

            return reservations

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return []
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)

    def get_reservations_by_vehicle_id(self, vehicle_id):
        reservations = []
        conn = None
        cursor = None
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM reservation WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            results = cursor.fetchall()

            for result in results:
                reservation = CarConnectReservation.Reservation(
                    reservation_id=result[0],
                    customer_id=result[1],
                    vehicle_id=result[2],
                    start_date=result[3],
                    end_date=result[4],
                    total_cost=result[5],
                    status=result[6]
                )
                reservations.append(reservation)

            return reservations

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return []
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                DBConnUtil.close_connection(conn)
