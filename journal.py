import datetime
from os import path
from os import listdir
import os 
import random
import journal_utils as j 

class Journal:

    def __init__(self,journal_name, dob, entries_path):
        self.journal_name = journal_name
        # password : todo
        self.dob = dob
        self.entries_path = entries_path # entries will be stored in this directory specified by the user
        # TODO: read this data from a config file, have a default value 

    def create_folder(self):
        pass


    def create_entry(self):
        """ Create a new entry: If user selects Y, will generate a date and time string
        which will be unique for every entry and will store the entry"""
        if not path.exists(self.entries_path):
             os.mkdir(self.entries_path)

        
        entry = input("Please type your entry in now, press enter when finished :> ")
        print()
        print(entry)
        print()
        confirm = j.get_confirmation("Does this like correct?(Y/N)")

        while True:

            if confirm.upper() == "Y":
                # create a new entry
                date_now = datetime.datetime.now()
                date_str = date_now.strftime("%Y-%m-%d %H:%M:%S")
                date_str+=".txt"
                
                with open(self.entries_path+"//"+date_str, "w") as f:
                    f.write(entry)

                return
            else:
                entry = input("Please type your entry in now, press enter when finished :> ")
                print()
                print(entry)
                print()
                confirm = j.get_confirmation("Does this look good? (y/n): :> ")

        
    def get_entry(self):

        year = j.get_date_input('year')
        month = j.get_date_input('month')
        day = j.get_date_input('day')
 
        if month < 10:
            month = "0" + str(month) # put in correct format

        if day < 10:
            day = "0" + str(day) # put in correct format

        date_str = str(year) + '-' + str(month) + '-' + str(day)
        my_path = ".//"+self.entries_path+"//"

        all_files = [f for f in listdir(my_path) if path.isfile(path.join(my_path, f))] # gets all entrys in directory
        relevent_files = []

        for file in all_files:
            if date_str in file:
                relevent_files.append(file)

        if len(relevent_files) > 1:
            print()
            print(" here are the entries for this date (please select one of the following)")
            print()
            for file in relevent_files:
                print("\t" + " * " + file)
           
            print()
            hour = j.get_date_input('hour')
            minutes = j.get_date_input('minutes')
            seconds = j.get_date_input('seconds')
            print()

            if hour < 10:
                hour = "0"+str(hour)
            if minutes < 10:
                minutes = "0"+str(minutes)
            if seconds < 10:
                seconds = "0"+str(seconds)
            
            time_str = str(hour) + ":" + str(minutes) + ":" + str(seconds) + ".txt"
            full_file_name = date_str + " " + time_str
            selected_file_name = ""

            for file in relevent_files:
                if full_file_name == file:
                    selected_file_name = file
            
            if selected_file_name != "":
                with open(self.entries_path+"//"+selected_file_name, "r") as f:
                    data = f.read()
                    print(data)
            else:
                print("No such file found")
        elif len(relevent_files) == 1:
            choice = j.get_confirmation("Only one entry found for this date, would you like to display it? (y/n) :> ")
        
            if choice.upper() == "Y":
                print()
                with open(self.encrypt_entries+"//"+relevent_files[0]) as f:
                    data = f.read()
                    print(data)
        else:
            print(" no entries for this date")
        print()


    def get_random_entry(self):

        my_path = ".//"+self.entries_path
        all_files = [f for f in listdir(my_path) if path.isfile(path.join(my_path, f))] # gets all entrys in directory
        relevent_files = []

        for file in all_files:
            if file.endswith(".txt"):
                relevent_files.append(file)

        if len(relevent_files) <= 0:
            print("No entries in directory")
            return

        random_choice = random.randint(0, len(relevent_files)-1)
        
        print()
        with open(self.entries_path+"//"+relevent_files[random_choice]) as f:
            data = f.read()
            print(data)
        print()
                

    def delete_entry(self):
        pass

    def login(self,username, password):
        pass

    def encrypt_entries(self):
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
    #print(" press 6 to log in")
    print()
    print("*" * 20)


            
def driver():

    display_prompt()
    my_journal = Journal("Bob","1999/09/09","my_entries")

    while True:
        choice = j.get_input_prompt()

        if choice == 1:
            my_journal.create_entry()
        elif choice == 2:
            my_journal.get_entry()
        elif choice == 3:
            my_journal.get_random_entry()
            pass
        elif choice == 4:
            #my_journal.delete_entry()
            pass
        elif choice == 5:
            return # terminate program execution
        elif choice == 6:
            #create a new acount/journal
            pass
        elif choice == 7:
            # login to an account/journal
            pass
        elif choice == 8:
            # forgot password or login
            pass
        
    

if __name__ == "__main__":
    driver() # start program 