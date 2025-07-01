import mysql.connector
from mysql.connector import Error

class DBConnUtil:
    @staticmethod
    def get_connection(connection_properties):
        try:
            connection = mysql.connector.connect(
                host=connection_properties['host'],
                database=connection_properties['database'],
                user=connection_properties['user'],
                password=connection_properties['password']
            )
            if connection.is_connected():
                # print("Connected to the database successfully")
                return connection
        except Error as e:
            print(f"Error while connecting to database: {e}")
            raise Exception("Database Connection Failed")

    @staticmethod
    def close_connection(connection):
        if connection.is_connected():
            connection.close()
            # print("Database connection closed")
