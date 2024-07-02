def get_input_prompt():
    """ Get a choice from the prompt menu from user """

    while True:
        try:
            choice = int(input("Enter choice :> "))
        except ValueError:
            print("Must provide a number")
        else:
            if choice < 1 or choice > 5:
                print("Please enter a valid choice")
            else:
                return choice
            
def get_date_input(construct):

    while True:
        if construct == 'year':
            while True:
                try:
                    choice = int(input("please enter a year :> "))
                except ValueError:
                    print("please enter a year in numerical format")
                else:
                    if choice > 2020 and choice < 2025:
                        return choice
                    else:
                        print("invalid year")
       
        elif construct == 'month':
            while True:
                try:
                    choice = int(input("please enter a month 1-12 :> "))
                except ValueError:
                    print("please enter a month in numerical format")
                else:
                    if choice > 0 and choice < 13:
                        return choice
                    else:
                        print("invalid month")

        elif construct == 'day':
            while True:
                try:
                    choice = int(input("please enter a day (1-31) :> "))
                except ValueError:
                    print("please enter a day in numerical format")
                else:
                    if choice > 0 and choice < 32:
                        return choice
                    else:
                        print("invalid day")
        
        elif construct == 'hour':
            while True:
                try:
                    choice = int(input("please enter an hour (0-23) :> "))
                except ValueError:
                    print("please enter an hour in numerical format")
                else:
                    if choice > 0 and choice <= 23:
                        return choice
                    else:
                        print("invalid hour")
        
        elif construct == 'minutes':
            while True:
                try:
                    choice = int(input("please enter minutes (0-59) :> "))
                except ValueError:
                    print("please enter minutes in numerical format")
                else:
                    if choice > 0 and choice <= 59:
                        return choice
                    else:
                        print("invalid minutes")

        elif construct == 'seconds':
            while True:
                try:
                    choice = int(input("please enter seconds (0-59) :> "))
                except ValueError:
                    print("please enter seconds in numerical format")
                else:
                    if choice > 0 and choice <= 59:
                        return choice
                    else:
                        print("invalid seconds")

  
def get_confirmation(message):

    while True:
        confirm = input(message)

        if confirm.upper() == 'Y' or confirm.upper() == 'N':
            return confirm
        else:
            print("invalid choice, please try again ")     
        