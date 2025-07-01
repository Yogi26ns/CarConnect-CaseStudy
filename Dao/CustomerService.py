import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil
from util.DBConnUtil import DBConnUtil
from CarConnect.entity import Customer as CarConnectCustomer
from Dao import ICustomerService as CarConnectICustomer
from CarConnect.exceptions import AuthenticationException as CarConnectAuthenticationException

class CustomerService(CarConnectICustomer.ICustomerService):
    def register_customer(self, customer):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = '''
                INSERT INTO customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            values = (
                customer.get_first_name(),
                customer.get_last_name(),
                customer.get_email(),
                customer.get_phone_number(),
                customer.get_address(),
                customer.get_username(),
                customer._Customer__password,
                customer.get_registration_date()
            )
            cursor.execute(query, values)
            conn.commit()

            print("\nCustomer registered successfully!")

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def get_customer_by_username(self, username):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = "SELECT * FROM customer WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                customer = CarConnectCustomer.Customer(
                    customer_id=result[0],
                    first_name=result[1],
                    last_name=result[2],
                    email=result[3],
                    phone_number=result[4],
                    address=result[5],
                    username=result[6],
                    password=result[7],
                    registration_date=result[8]
                )
                return customer
            else:
                return None

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def authenticate_customer(self, username, password):
        customer = self.get_customer_by_username(username)
        if customer is not None and customer.authenticate(password):
            return customer
        else:
            raise CarConnectAuthenticationException.AuthenticationException("Invalid username or password.")

    def update_customer_profile(self, customer_id, field, new_value):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = f"UPDATE customer SET {field} = %s WHERE CustomerID = %s"
            cursor.execute(query, (new_value, customer_id))
            conn.commit()

            if cursor.rowcount > 0:
                # print("\nProfile updated successfully!")
                return True
            else:
                print("\nUpdate failed. Please try again.")
                return False

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def get_customer_by_id(self, customer_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()

            query = 'SELECT * FROM customer WHERE CustomerID = %s'
            cursor.execute(query, (customer_id,))
            result = cursor.fetchone()

            if result:
                customer = CarConnectCustomer.Customer(
                    customer_id=result[0],
                    first_name=result[1],
                    last_name=result[2],
                    email=result[3],
                    phone_number=result[4],
                    address=result[5],
                    username=result[6],
                    password=result[7],
                    registration_date=result[8]
                )
                return customer
            else:
                return None

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)

    def delete_customer(self, customer_id):
        try:
            connection_properties = DBPropertyUtil.get_connection_properties()
            conn = DBConnUtil.get_connection(connection_properties)
            cursor = conn.cursor()
            query = "DELETE FROM customer WHERE CustomerID = %s"
            cursor.execute(query, (customer_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print("\nCustomer deleted successfully!")
                return True
            else:
                print("\nCustomer not found!")
                return False

        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
            return False
        finally:
            if conn.is_connected():
                cursor.close()
                DBConnUtil.close_connection(conn)
