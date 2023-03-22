import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as error:
        print(f"Error: {error}")

    return connection


def execute_query(connection, query):
    """Executes a query to create or insert date into database

    Args:
        connection (connection): Connection to DB
        query (str): SQL query
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as error:
        print(f"Error: {error}")


def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        surname VARCHAR(30),
        email TEXT(50),
        phone VARCHAR(15),
        gender VARCHAR(7)
    )
    """
    execute_query(connection, query)


def execute_read_query(connection, query):
    """Executes a query to get data from database

    Args:
        connection (connection): Connection to DB
        query (str): SQL query
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as error:
        print(f"Error: {error}")
