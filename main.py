import funcs
import sql_connection

connection = sql_connection.create_connection('contact management/info.db')
sql_connection.create_table(connection)

print("This is a contact management system")
print("Every contact has:")
print(f"\t{'Name' :<20}: no longet than 30 letters and can't be empty")
print(f"\t{'Surname' :<20}: no longet than 30 letters or could be empty")
print(f"\t{'Email' :<20}: 'exapmle@anymail.com' or could be emply")
print(f"\t{'Phone Number' :<20}: '+374 -- --- ---' and can't be empty")
print(f"\t{'Gender' :<20}: male/female or could be emply\n")

print("There are several commands you can use:")
print(f"\t{'add contact' :<20}: to add contact of a person")
print(f"\t{'get contact' :<20}: to get contact of a person ")
print(f"\t{'delete contact' :<20}: to delete contact of a person ")
print(f"\t{'view contacts' :<20}: to view all contacts ")


command = input("Enter the command: ")
command_list = {'add contact': funcs.add,
                'get contact': funcs.get,
                'delete contact': funcs.delete,
                'view contacts': funcs.view,
                }


while command != "exit":
    if command in command_list:
        command_list[command](connection)
    else:
        print("Command not found\n Enter correct command i.e. \
    (add contact, get contact, delete contact, view contacts list, exit)")
    command = input("Enter the command: ")
