# Contact Management Terminal App

This is a simple terminal application for managing contacts. With this app, you can easily add, view, get, and delete contacts.

## Commands
### The following commands are available in the app:

* 'add contact' - To add a new contact.
* 'get contact' - To get the details of a specific contact.
* 'delete contact' - To delete a contact.
* 'view contacts' - To view all saved contacts.
* 'exit' - To exit the app.

## Contact Attributes
### Each contact has the following attributes:

* 'ID' - Unique number for each contact
* 'Name' - A string no longer than 30 letters and can't be empty.
* 'Surname' - A string no longer than 30 letters or could be empty.
* 'Email' - A string in the format of example@anymail.com or could be empty.
* 'Phone Number' - A string in the format of +37490000000 and can't be empty.
* 'Gender' - A string, either "male" or "female", or could be empty.


## Usage
### To use the app, simply run the app.py file in a terminal:

> python3 app.py


## Example
```
$ add contact
  Name: John
  Surname: Doe
  Email: john.doe@example.com
  Phone Number: +37499000000
  Gender: Male
  Contact added successfully!

$ get contact
  Name: John
  Surname: Doe
  Email: john.doe@example.com
  Phone Number: +37499000000
  Gender: Male

$ delete contact
  Name: John
  Contact deleted successfully!

  $ view contacts
  Name: John
  Surname: Doe
  Email: john.doe@example.com
  Phone Number: +37499000000
  Gender: Male
```
