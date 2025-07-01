import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil
from CarConnect.entity import Admin as CarConnectAdmin
from Dao import IAdminService as CarConnectIAdmin
from CarConnect.exceptions import AdminNotFoundException as CarConnectAdminNotFoundException
from CarConnect.exceptions import AuthenticationException as CarConnectAuthenticationException

class AdminService(CarConnectIAdmin.IAdminService):
    def get_admin_by_username(self, username):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()
            query = 'SELECT * FROM admin WHERE username = %s'
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                admin = CarConnectAdmin.Admin(
                    admin_id=result[0],
                    first_name=result[1],
                    last_name=result[2],
                    email=result[3],
                    phone_number=result[4],
                    username=result[5],
                    password=result[6],
                    role=result[7],
                    join_date=result[8]
                )
                return admin
            else:
                raise CarConnectAdminNotFoundException.AdminNotFoundException("Admin with given username not found.")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def authenticate_admin(self, username, password):
        try:
            admin = self.get_admin_by_username(username)
            if admin.authenticate(password):
                return admin
            else:
                raise CarConnectAuthenticationException.AuthenticationException("Invalid password.")
        except CarConnectAdminNotFoundException.AdminNotFoundException as e:
            print(e)
            raise
        except CarConnectAuthenticationException.AuthenticationException as e:
            print(e)
            raise

    # AdminService.py (add these inside the class)
    def get_admin_by_id(self, admin_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = 'SELECT * FROM admin WHERE AdminID = %s'
            cursor.execute(query, (admin_id,))
            result = cursor.fetchone()

            if result:
                admin = CarConnectAdmin.Admin(
                    admin_id=result[0],
                    first_name=result[1],
                    last_name=result[2],
                    email=result[3],
                    phone_number=result[4],
                    username=result[5],
                    password=result[6],
                    role=result[7],
                    join_date=result[8]
                )
                return admin
            else:
                return None

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def register_admin(self, admin):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = '''
                    INSERT INTO admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) \
                    '''
            values = (
                admin.get_first_name(),
                admin.get_last_name(),
                admin.get_email(),
                admin.get_phone_number(),
                admin.get_username(),
                admin.get_password(),
                admin.get_role(),
                admin.get_join_date()
            )
            cursor.execute(query, values)
            conn.commit()
            print("\nAdmin registered successfully!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def update_admin(self, admin_id, field, new_value):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = f"UPDATE admin SET {field} = %s WHERE AdminID = %s"
            cursor.execute(query, (new_value, admin_id))
            conn.commit()

            if cursor.rowcount > 0:
                print("\nAdmin profile updated successfully!")
                return True
            else:
                print("\nUpdate failed. Please try again.")
                return False

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def delete_admin(self, admin_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "DELETE FROM admin WHERE AdminID = %s"
            cursor.execute(query, (admin_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print("\nAdmin deleted successfully!")
                return True
            else:
                print("\nAdmin not found!")
                return False

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)
