import journal
import database_utils as du
import sys

####################################################################################################################
# TODO Tomorrow
# create hash of the password with a hashing library maybe sha256
# then store this hash in the database as password
#
# when reading the password we will also need to hash the inputted password then compare the two hashes for equality
####################################################################################################################

def display_prompt(username):
    print("*" * 60)
    print("\t" * 3, "WELCOME TO YOUR JOURNAL {}".format(username).upper(), "\t" * 3)
    print()
    print(" \tpress 1 to create a new entry ")
    print(" \tpress 2 to select an existing entry ")
    print(" \tpress 3 to select a random entry ")
    print(" \tpress 4 to delete an existing entry ")
    print(" \tpress 5 to log out ")
    print(" \tpress 6 to exit the program ")
    print()
    print("*" * 60)

def display_login():
    print("*" * 60)
    print("\t" * 3, "WELCOME TO YOUR JOURNAL ", "\t" * 3)
    print()
    print(" \tpress 1 to log in")
    print(" \tpress 2 to create an account")
    print(" \tpress 3 to exit the program ")
    print()
    print("*" * 60)

def driver_logged_in(my_journal,username):
   
    display_prompt(username)
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
            return # log out, return back to main screen
        elif choice == 5:
            sys.exit() # terminate program execution
                
            
def driver():

    my_journal = journal.Journal("Default","1999/09/09")
    display_login()

    while True:
        choice = journal.j.get_input_prompt()
        
        if choice == 1:
            logged_in,username = du.login()
            if logged_in: # successful login
                driver_logged_in(my_journal,username)
            else:
                print("Wrong password")
                print()
        elif choice == 2:
            du.create_account()
        elif choice == 3:
            return # terminate the program
        elif choice == 4:
            # forgot password or login
            pass
        

if __name__ == "__main__":
    driver() # start program 