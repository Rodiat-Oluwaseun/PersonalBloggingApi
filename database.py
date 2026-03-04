import mysql.connector
from mysql.connector import Error

# Base class for Database logic (Requirement: Inheritance)


class DatabaseConnection:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "Atandayemi@25",
            "database": "blogging_api"
        }

    def get_connection(self):
        # Requirement: Exception Handling
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
