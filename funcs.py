from validate import Validatior
from sql_connection import DB

db = None


def repr(contacts):
    for contact in contacts:
        print(contact)


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

    if email:
        query = f"""
        INSERT INTO contacts (name,surname,email,phone,gender)
        VALUES ('{name}','{surname if surname else 'NULL'}','{email if email else 'NULL'}','{phone}','{gender if gender else 'NULL'}')
        """
    else:
        query = f"""
        INSERT INTO contacts (name,surname,email,phone,gender)
        VALUES ('{name}','{surname if surname else 'NULL'}',NULL,'{phone}','{gender if gender else 'NULL'}')
        """
    db.execute_query(query)
    print("Contact added successfully!")


def get():
    clause = ''
    tmpdict = {'name': input(f"\t{'Enter the Name':<25}:"),
               'surname': input(f"\t{'Enter the Surname':<25}:"),
               'email': input(f"\t{'Enter the Email':<25}:"),
               'phone': input(f"\t{'Enter the Phone Number':<25}:"),
               'gender': input(f"\t{'Enter the Gender':<25}:")}
    for i, val in tmpdict.items():
        if val:
            clause += f"{i}='{val}' AND "
    contact_list = db.execute_read_query(f"""SELECT * 
                                    FROM contacts
                                    WHERE {clause}TRUE""")
    if contact_list:
        repr(contact_list)
    else:
        print("No such contact")


def delete():
    print("If you dont know the 'id' of the contact press 'Enter'\n\
        Find it with 'get contact' and then delete it")
    if id := input("Enter the id: "):
        query = f"""DELETE FROM contacts
                    WHERE id = {id}"""
        db.execute_query(query)
        print("Contact deleted successfully!")


def view():
    repr(db.execute_read_query("""SELECT * FROM contacts"""))
