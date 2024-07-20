import datetime
from os import path
from os import listdir
import os 
import random
import journal_utils as j 
import json

class Journal:

    def __init__(self,journal_name, dob):
        self.journal_name = journal_name
        self.dob = dob
        config_file = open("config.json", "r")
        config_json = json.load(config_file)
        self.default_path = config_json["DEFAULT_PATH"] # boolean value: is using default path?
        self.entries_path = config_json["ENTRIES_PATH"] # entries will be stored in this directory specified by the user
        config_file.close()


    def list_entries(self):
        year = j.get_date_input('year')
        month = j.get_date_input('month')
        day = j.get_date_input('day')
        rev_file_count = None
        selected_file_name = ""
 
        if month < 10:
            month = "0" + str(month) # put in correct format

        if day < 10:
            day = "0" + str(day) # put in correct format

        date_str = str(year) + '-' + str(month) + '-' + str(day)

        if self.default_path:
            my_path = ".//"+self.entries_path+"//"

        all_files = [f for f in listdir(my_path) if path.isfile(path.join(my_path, f))] # gets all entrys in directory
        relevent_files = []

        for file in all_files:
            if date_str in file:
                relevent_files.append(file)

        rev_file_count = len(relevent_files)

        if rev_file_count > 1:
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

            for file in relevent_files:
                if full_file_name == file:
                    selected_file_name = file
       
        elif rev_file_count == 1:
            selected_file_name = relevent_files[0]

        return selected_file_name, rev_file_count

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
                file_path = self.entries_path+"//"+date_str
                
                with open(file_path, "w") as f:
                    f.write(entry)

                return # We can return as we have successfully created a new entry
            else:
                entry = input("Please type your entry in now, press enter when finished :> ")
                print()
                print(entry)
                print()
                confirm = j.get_confirmation("Does this look good? (y/n): :> ")

        
    def get_entry(self):

        selected_file_name,relevent_files_count = self.list_entries()
        #print("selected_file_name : " + selected_file_name, "relevent_files_count : ",relevent_files_count)
        
        if relevent_files_count == 0:
            print(" no entries for this date")
            print()
        
        elif relevent_files_count == 1:
            choice = j.get_confirmation("Only one entry found for this date, would you like to display it? (y/n) :> ")
        
            if choice.upper() == "Y":
                print()
                with open(self.entries_path+"//"+selected_file_name,"r") as f:
                    data = f.read()
                    print(data)
            
        elif relevent_files_count > 1:
            print()
            with open(self.entries_path+"//"+selected_file_name, "r") as f:
                data = f.read()
                print(data)
        else:
            print("No such file found")
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
            print()
            print("*" * 60)
            print("\t"*2, " Journal entry : ", relevent_files[random_choice])
            print()
            print(data)
        print()
                

    def delete_entry(self):

        selected_file_name,relevent_files_count = self.list_entries()

        if relevent_files_count == 0:
            print("No file found")
            return False
        
        # delete entry
        full_path = self.entries_path + "/" + selected_file_name

        choice = input("Are you sure you want to delete this file?")
        if choice.upper() == "Y":
            os.remove(full_path)
            return True
        else:
            return False
        
    def delete_account():
        # Ask user for password again
        # Ask user if they are certain, i.e. this action is not reversible
        # Delete entries for user
        # Delete user from database
        # prompt success and log user out
        pass
