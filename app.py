import funcs

funcs.create_DB('info.db')


print("This is a contact management system")
print("Every contact has:")
print(f"\t{'Name' :<20}: no longer than 30 letters and can't be empty")
print(f"\t{'Surname' :<20}: no longer than 30 letters or could be empty")
print(f"\t{'Email' :<20}: 'exapmle@anymail.com' or could be empty")
print(f"\t{'Phone Number' :<20}: '+37490000000' and can't be empty")
print(f"\t{'Gender' :<20}: male/female or could be empty\n")

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
        command_list[command]()
    else:
        print("Command not found\n Enter correct command i.e. \
            (add contact, get contact, delete contact, view contacts, exit)")
    command = input("Enter the command: ")
