import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil
from CarConnect.entity import Vehicle as CarConnectVehicle
from CarConnect.Dao import IVehicleService as CarConnectIVehicle
from CarConnect.exceptions import VehicleNotFoundException as CarConnectVehicleNotFoundException

class VehicleService(CarConnectIVehicle.IVehicleService):
    def add_vehicle(self, vehicle):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = '''
                INSERT INTO vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate,Category)
                VALUES (%s, %s, %s, %s, %s, %s, %s,%s)
            '''
            values = (
                vehicle.get_model(),
                vehicle.get_make(),
                vehicle.get_year(),
                vehicle.get_color(),
                vehicle.get_registration_number(),
                vehicle.is_available(),
                vehicle.get_daily_rate(),
                vehicle.get_category()
            )

            cursor.execute(query, values)
            conn.commit()
            print("\nVehicle added successfully!")
            return True
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def get_all_vehicles(self):
        vehicles = []
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM vehicle"
            cursor.execute(query)
            results = cursor.fetchall()

            for result in results:
                vehicle = CarConnectVehicle.Vehicle(
                    vehicle_id=result[0],
                    model=result[1],
                    make=result[2],
                    year=result[3],
                    color=result[4],
                    registration_number=result[5],
                    availability=result[6],
                    daily_rate=result[7],
                    category=result[8]
                )
                vehicles.append(vehicle)

            return vehicles

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def update_vehicle(self, vehicle_id, new_daily_rate):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "UPDATE vehicle SET DailyRate = %s WHERE VehicleID = %s"
            cursor.execute(query, (new_daily_rate, vehicle_id))
            conn.commit()

            if cursor.rowcount == 0:
                raise CarConnectVehicleNotFoundException.VehicleNotFoundException("Vehicle ID not found.")
            else:
                print("\nVehicle daily rate updated successfully!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def delete_vehicle(self, vehicle_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "DELETE FROM vehicle WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            conn.commit()

            if cursor.rowcount == 0:
                raise CarConnectVehicleNotFoundException.VehicleNotFoundException("Vehicle ID not found.")
            else:
                print("\nVehicle deleted successfully!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def is_vehicle_active(self, vehicle_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT Availability FROM vehicle WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            result = cursor.fetchone()

            if result and result[0] == 1:  # Available
                return True
            else:
                return False

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def get_vehicle_daily_rate(self, vehicle_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT DailyRate FROM vehicle WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            result = cursor.fetchone()

            if result:
                return result[0]  # Return daily rate
            else:
                return None

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def mark_vehicle_unavailable(self, vehicle_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "UPDATE vehicle SET Availability = 0 WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            conn.commit()

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def get_available_vehicles(self):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()
            query = "SELECT * FROM vehicle WHERE Availability = TRUE"
            cursor.execute(query)
            results = cursor.fetchall()

            vehicles = []
            from CarConnect.entity import Vehicle as CarConnectVehicle
            for result in results:
                vehicle = CarConnectVehicle.Vehicle(
                    vehicle_id=result[0],
                    model=result[1],
                    make=result[2],
                    year=result[3],
                    color=result[4],
                    registration_number=result[5],
                    availability=result[6],
                    daily_rate=result[7],
                    category=result[8]
                )
                vehicles.append(vehicle)
            return vehicles

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return []
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def update_vehicle(self, vehicle_id, new_daily_rate):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "UPDATE vehicle SET DailyRate = %s WHERE VehicleID = %s"
            cursor.execute(query, (new_daily_rate, vehicle_id))
            conn.commit()

            if cursor.rowcount > 0:
                print("\nVehicle daily rate updated successfully!")
                return True  # ✅ Added this
            else:
                print("\nUpdate failed. Vehicle not found.")
                return False

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def get_vehicle_by_id(self, vehicle_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM vehicle WHERE VehicleID = %s"
            cursor.execute(query, (vehicle_id,))
            result = cursor.fetchone()

            if result:
                vehicle = CarConnectVehicle.Vehicle(
                    vehicle_id=result[0],
                    model=result[1],
                    make=result[2],
                    year=result[3],
                    color=result[4],
                    registration_number=result[5],
                    availability=bool(result[6]),
                    daily_rate=float(result[7]),
                    category=result[8]
                )
                return vehicle
            else:
                return None

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)
