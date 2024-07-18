import journal
import sys
from getpass import getpass
from mysql.connector import connect, Error, cursor


def login():
   # To do allow a user to login
   
   # Ask user for username,
   # get username from database
   # Ask user for password
   # Get password from database

   return True

def create_account():
    # FIRST connect to database
    # read username and password from config file
    try:
        with connect(
                     host="localhost",
                     user="",
                     password="",
                     ) as connection:
            # connecction successful
            while True:
                username = input("Enter username")
                db_cursor= connection.cursor()
                query = "USE journal;"
                db_cursor.execute(query)
                username_formated = "'{}'".format(username)
                query = "SELECT userName FROM users WHERE EXISTS(SELECT * FROM users WHERE userName = {})".format(username_formated)
                db_cursor.execute(query)
                rows=db_cursor.fetchall() # gets the output rows from the above query
            
                if len(rows) == 1: # if one row exists this means this username is taken
                    print("User already exists: Please re-enter another username")
                else:
                    break # user available: break out of the loop and continue creating account 
            

            

    except Error as e:
        print(e)
        raise Exception("Could not connect to database")

    # 1: Get username from user
    # 2: check if username is already in database/exists
    # 3: if user already exists prompt user for a new name and tell username already exists
    # 4: if avaiaible store username in databse and prompt user for password
    # 5: store password in databse
    pass

def encrypt_entries():
    pass

def display_prompt():
    print("*" * 20)
    print("\t" * 3, "WELCOME TO YOUR JOURNAL", "\t" * 3)
    print()
    print()
    print(" press 1 to create a new entry ")
    print(" press 2 to select an existing entry ")
    print(" press 3 to select a random entry ")
    print(" press 4 to delete an existing entry ")
    print(" press 5 to exit the program ")
    print()
    print("*" * 20)

def display_login():
    print("*" * 20)
    print("\t" * 3, "WELCOME TO YOUR JOURNAL", "\t" * 3)
    print()
    print()
    print(" press 1 to log in")
    print(" press 2 to create an account")
    print(" press 3 to exit the program ")
    print()
    print("*" * 20)

def driver_logged_in(my_journal):
   
    display_prompt()
    while True:
        choice = journal.j.get_input_prompt()

        if choice == 1:
            my_journal.create_entry()
        elif choice == 2:
            my_journal.get_entry()
        elif choice == 3:
            my_journal.get_random_entry()
        elif choice == 4:
            my_journal.delete_entry()
        elif choice == 5:
            sys.exit() # terminate program execution
                
            
def driver():

    create_account()
    my_journal = journal.Journal("Default","1999/09/09","my_entries")
    display_login()

    while True:
        choice = journal.j.get_input_prompt()
        
        if choice == 1:
            logged_in = login()
            if logged_in:
                driver_logged_in(my_journal)
        elif choice == 2:
            create_account()
        elif choice == 3:
            return # terminate the program
        elif choice == 4:
            # forgot password or login
            pass
        

if __name__ == "__main__":
    driver() # start program 