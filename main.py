import journal
import database_utils as du
import sys
import os

####################################################################################################################
# TODO Tomorrow OR later
# 
# Encrypt users entries using users password as the key
# Allow the user the option to unencrypt all the entries[display wanrning: other users can view your entries]
####################################################################################################################

def display_prompt(username):
    print("*" * 60)
    print("\t" * 2, "WELCOME TO YOUR JOURNAL {}".format(username).upper(), "\t" * 3)
    print()
    print(" \tpress (1) to create a new entry ")
    print(" \tpress (2) to select an existing entry ")
    print(" \tpress (3) to select a random entry ")
    print(" \tpress (4) to delete an existing entry ")
    print(" \tpress (5) to log out ")
    print(" \tpress (6) to exit the program ")
    print(" \tpress (7) to delete journal")
    print()
    print("*" * 60)

def display_login():
    print("*" * 60)
    print("\t" * 2, "WELCOME TO YOUR JOURNAL ", "\t" * 3)
    print()
    print(" \tpress (1) to log in")
    print(" \tpress (2) to create an account")
    print(" \tpress (3) to exit the program ")
    print()
    print("*" * 60)

def driver_logged_in(my_journal,username):
   
    
    while True:
        os.system('clear')# Linux: also allow for windows users
    
        display_prompt(username)
        choice = journal.j.get_input_prompt(7)

        if choice == 1:
            my_journal.create_entry()
        elif choice == 2:
            my_journal.get_entry()
        elif choice == 3:
            my_journal.get_random_entry()
        elif choice == 4:
            my_journal.delete_entry()
        elif choice == 5:
            return # log out, return back to main screen
        elif choice == 6:
            sys.exit() # terminate program execution
        elif choice == 7:
            # delete journal
            log_out = du.delete_account(my_journal)
            if log_out: # account was deleted, log out
                return
            
          
def driver():

    my_journal = journal.Journal("Default","1999/09/09") # initiliaze journal to default account
    
    while True:
        os.system('clear')
        display_login()
        choice = journal.j.get_input_prompt(3)
        
        if choice == 1:
            logged_in,username = du.login()
            my_journal = journal.Journal(username,None)
            if logged_in: # successful login
                driver_logged_in(my_journal,username)
            else:
                print("Incorrect password or User not Found")
                print()
            # If we reach this point then we must have logged out
            my_journal = journal.Journal("Default","1999/09/09") # since logged out, reset journal to default account
        elif choice == 2:
            du.create_account()
        elif choice == 3:
            return # terminate the program
        elif choice == 4:
            # forgot password or login
            pass
        

if __name__ == "__main__":
    driver() # start program 