import validate
import sql_connection


def add(connection):
    name = input(f"\t{'Enter the Name':<25}:")
    while not validate.isValidName(name):
        print("Wrong Name format")
        name = input(f"\t{'Enter the Name':<25}:")

    surname = input(f"\t{'Enter the Surname':<25}:")
    while not validate.isValidSurname(surname):
        print("Wrong Surname format")
        surname = input(f"\t{'Enter the Surname':<25}:")

    email = input(f"\t{'Enter the Email':<25}:")
    while not validate.isValidEmail(email):
        print("Wrong Email format")
        email = input(f"\t{'Enter the Email':<25}:")

    phone = input(f"\t{'Enter the Phone Number':<25}:")
    while not validate.isValidPhone(phone):
        print("Wrong Phone Number format")
        phone = input(f"\t{'Enter the Phone Number':<25}:")

    gender = input(f"\t{'Enter the Gender':<25}:")
    while not validate.isValidGender(gender):
        print("Wrong Geneder format")
        gender = input(f"\t{'Enter the Gender':<25}:")
    query = f"""
    INSERT INTO contacts (name,surname,email,phone,gender)
    VALUES ('{name}','{surname}','{email}','{phone}','{gender}')
    """
    sql_connection.execute_query(connection, query)


def get(connection):
    print(sql_connection.execute_read_query(connection, f"""SELECT * 
                                                            FROM contacts
                                                            WHERE """))
    pass

def delete(connection):
    pass


def view(connection):
    print(sql_connection.execute_read_query(
        connection, """SELECT * FROM contacts"""))
