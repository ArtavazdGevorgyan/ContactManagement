import sqlite3
from sqlite3 import Error


class DB:
    indicator = None

    def __init__(self, path='info.db'):
        self.__connection = self.__create_connection(path)
        self.__create_table()

    def __new__(cls, *args):
        if cls.indicator == None:
            cls.indicator = super().__new__(cls)
        return cls.indicator

    def __create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except Error as error:
            print(f"Error: {error}")

        return connection

    def execute_query(self, query):
        """Executes a query to create or insert date into database

        Args:
            query (str): SQL query
        """
        cursor = self.__connection.cursor()
        try:
            cursor.execute(query)
            self.__connection.commit()
        except Error as error:
            print(f"Error: {error}")

    def __create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30) NOT NULL,
            surname VARCHAR(30),
            email TEXT(50) UNIQUE,
            phone VARCHAR(15) UNIQUE,
            gender VARCHAR(7)
        )
        """
        self.execute_query(query)

    def execute_read_query(self, query):
        """Executes a query to get data from database

        Args:
            query (str): SQL query
        """
        try:
            cursor = self.__connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as error:
            print(f"Error: {error}")
