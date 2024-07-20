from getpass import getpass
from mysql.connector import connect, Error, cursor
import json
import hashlib

#globals
config_file = open("config.json", "r")
config_json = json.load(config_file)
DB_HOST = config_json['DB_HOST']
DB_USER = config_json['DB_USER']
DB_PASSWORD = config_json['DB_PASSWORD']

def get_password():
    
    while True:
     password = getpass("Enter a password :> ", stream=None)
     print()
     if len(password) < 7:
        print("Password must be at least seven characaters long ")
        print()
     else:
        return password #valid password: return from function

def user_exists(username,db_cursor):
    
    username_formated = "'{}'".format(username)
    query = "SELECT userName FROM users WHERE userName = {}".format(username_formated)
    db_cursor.execute(query)
    rows=db_cursor.fetchall() # gets the output rows from the above query
            
    if len(rows) == 1: # if one row exists this means this username is taken
        return True
    else:
        return False # user available: break out of the loop and continue creating account

     
def login():
   # To do allow a user to login

   try:
        with connect(
                     host=DB_HOST, 
                     user=DB_USER,
                     password=DB_PASSWORD
                     ) as connection:
            
            # connecction successful
            db_cursor= connection.cursor()
            query = "USE journal;"
            db_cursor.execute(query)
            username = ""

            while True:
                username = input("Enter username :> ")
                print()
                if(user_exists(username,db_cursor)):
                    break # user exists: break out of loop
                else:
                    print("User not found")
                    print()
            # user found
            username_formated = "'{}'".format(username)
            query = "SELECT user_pass FROM users WHERE userName = {}".format(username_formated)
            db_cursor.execute(query)
            rows=db_cursor.fetchall()
            correct_pass = rows[0][0] # hashed password from database 
            password = get_password() # get password inputted by user
            password_input_hex = hashlib.sha256(password.encode('utf-8')).hexdigest() # convert to hash
            
            return (True,username) if password_input_hex == correct_pass else (False, "")
   except Error as e:
        print(e)
        raise Exception("Could not connect to database")
   

def create_account():
    # FIRST connect to database -> Done
    # read username and password from config file
    try:
        with connect(
                     host=DB_HOST, 
                     user=DB_USER,
                     password=DB_PASSWORD
                     ) as connection:
            # connecction successful
            db_cursor= connection.cursor()
            username = ""
            while True:
                username = input("Enter username :> ")
                print()
                query = "USE journal;"
                db_cursor.execute(query)

                if user_exists(username, db_cursor):
                    print("User already exists: Please re-enter another username")
                    print()
                else:
                    break # username is available: break from loop
            # username is available
            password = get_password()
            password_hex = hashlib.sha256(password.encode('utf-8')).hexdigest() # hash password before storing
            # TODO add more fields: DOB, account creation time, account creation date, gender, etc...
            username = "'{}'".format(username) # put in correct format for SQL query
            password_hex = "'{}'".format(password_hex) # put in correct format for SQL query
            query = "INSERT INTO users(userName,user_pass) VALUES({},{})".format(username, password_hex)
            db_cursor.execute(query)
            connection.commit() # commit changes to database through our connection object
            print()
            print("Journal user successfully created")
            print()
    except Error as e:
        print(e)
        raise Exception("Could not connect to database")


def encrypt_entries():
    pass