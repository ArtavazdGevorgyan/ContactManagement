from validate import Validatior
from sql_connection import DB

db = None


def create_DB(path):
    global db
    db = DB(path)


def add():
    name = input(f"\t{'Enter the Name':<25}:")
    while not Validatior.isValidName(name):
        print("Wrong Name format")
        name = input(f"\t{'Enter the Name':<25}:")

    surname = input(f"\t{'Enter the Surname':<25}:")
    while not Validatior.isValidSurname(surname):
        print("Wrong Surname format")
        surname = input(f"\t{'Enter the Surname':<25}:")

    email = input(f"\t{'Enter the Email':<25}:")
    while not Validatior.isValidEmail(email):
        print("Wrong Email format")
        email = input(f"\t{'Enter the Email':<25}:")

    phone = input(f"\t{'Enter the Phone Number':<25}:")
    while not Validatior.isValidPhone(phone):
        print("Wrong Phone Number format")
        phone = input(f"\t{'Enter the Phone Number':<25}:")

    gender = input(f"\t{'Enter the Gender':<25}:")
    while not Validatior.isValidGender(gender):
        print("Wrong Geneder format")
        gender = input(f"\t{'Enter the Gender':<25}:")

    query = f"""
    INSERT INTO contacts (name,surname,email,phone,gender)
    VALUES ('{name}','{surname if surname != '' else 'NULL'}','{email}','{phone}','{gender if gender != '' else 'NULL'}')
    """
    db.execute_query(query)


def get():
    print(db.execute_read_query(f"""SELECT * 
                                    FROM contacts
                                    WHERE """))
    pass


def delete():
    pass


def view():
    print(db.execute_read_query("""SELECT * FROM contacts"""))
