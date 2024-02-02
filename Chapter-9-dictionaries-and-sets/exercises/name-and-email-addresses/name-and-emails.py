'''
write a program that keeps the names and email addresses of people in a dictionary as key-value pairs.
the program should display a menu that lets the user do the following:

1. look up an email address
2. add a new name and email address
3. change an existing email address
4. delete an existing name and email address

The program should pickle the dictionary and save it to a file when the user exits the program.

Each time the program starts, it should retrieve the dictionary from file and unpickle it.
'''

import re
import pickle
import os

LOOK_UP_NAME_EMAIL_PAIR = 'LOOK UP'
ADD_NEW_NAME_EMAIL_PAIR = 'ADD'
CHANGE_EXISTING_EMAIL = 'CHANGE'
DELETE_EXISTING_NAME_EMAIL_PAIR = 'DELETE'
QUIT = 'QUIT'

CURRENT_DIRECTORY = os.getcwd() + '\\Chapter-9-dictionaries-and-sets\\exercises\\name-and-email-addresses\\'
def main():
    
    names_and_emails = unpickle()

    process_choice(names_and_emails)

def get_menu_choice():
    print_menu()

    choice = input('Enter your choice: ')

    while (choice not in (LOOK_UP_NAME_EMAIL_PAIR,
                          ADD_NEW_NAME_EMAIL_PAIR,
                          CHANGE_EXISTING_EMAIL,
                          DELETE_EXISTING_NAME_EMAIL_PAIR,
                          QUIT)):
        print_menu()
        choice = input('Enter a valid choice: ')

    return choice

def print_menu():
    print()
    print('Names and Emails List')
    print('---------------------')
    print('Type LOOK UP to look up a name and email.')
    print('Type ADD to add a name and email.')
    print('Type CHANGE to modify an existing email.')
    print('Type DELETE to delete an existing email.')
    print('Type QUIT to quit program')
    print()

def process_choice(name_and_emails):
    choice = get_menu_choice()
    while (choice not in QUIT):
        if choice == LOOK_UP_NAME_EMAIL_PAIR:
            look_up(name_and_emails)
        elif choice == ADD_NEW_NAME_EMAIL_PAIR:
            add_to_email_dict(name_and_emails)
        elif choice == CHANGE_EXISTING_EMAIL:
            change_email(name_and_emails)
        elif choice == DELETE_EXISTING_NAME_EMAIL_PAIR:
            delete_email(name_and_emails)
        choice = get_menu_choice()
    serialize(name_and_emails)

def look_up(name_email_dictionary):
    name = input('Enter a name to look up')
    print(name_email_dictionary.get(name,'Name not found'))

def add_to_email_dict(name_email_dictionary):
    name = input('Enter a name to add: ')
    email = input('Enter an email address: ')
    while not valid_email(email):
        email = input('Error. Email string \'{email}\' not valid. Re-enter an email: ')

    if name not in name_email_dictionary:
        name_email_dictionary[name] = email
    else:
        print('Name already exists in list.')

def change_email(name_email_dictionary):
    name = input('Enter a name of the email you wish to change: ')
    if name in name_email_dictionary:
        email = input('Enter a new email: ')
        while not valid_email(email):
            email = input('Error. Email string \'{email}\' not valid. Re-enter an email: ')
        name_email_dictionary[name] = email
    else:
        print('Name was not found.')

def delete_email(name_email_dictionary):
    name = input('Enter a name of the email you wish to delete: ')
    if name in name_email_dictionary:
        del name_email_dictionary[name]
    else:
        print('Name not found')

def valid_email(email_entry):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if(re.fullmatch(regex,email_entry)):
        return True
    else:
        return False
    
def unpickle():
    name_and_emails = {}
    end_of_file = False

    input_file = open(CURRENT_DIRECTORY + 'emails.dat', 'rb')

    while not end_of_file:
        try:
            name_and_emails = pickle.load(input_file)
        except EOFError:
            end_of_file = True
    input_file.close()
    return name_and_emails

def serialize(name_and_emails):
    output_file = open(CURRENT_DIRECTORY + 'emails.dat','wb')
    pickle.dump(name_and_emails,output_file)
main()