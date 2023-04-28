from prettytable import from_csv
from modify_roster import modify_roster

def view_schedule():
   
    print("\nRoster for the following week: \n")
    with open('schedule_record.csv') as table_file:
        roster_tab = from_csv(table_file)
    print(roster_tab)

    print("\nUnavailability record: \n")
    with open('ua_record.csv') as ua_table_file:
        ua_tab = from_csv(ua_table_file)
    print(ua_tab)

    
    print("\n")

    print("If you are happy with the above work schedule, please enter 'Yes' to confirm or 'No' if you wish to make changes.")
    while True: 
        confirm_or_not = input("Would you like to confirm your work schedule? ")
        if confirm_or_not == "Yes": 
            print("\n")
            print("+--------------------------------------------------------------------------------------------------+")
            print("| Thank you for your coorporation! You have completed your work schedule for the next 2 weeks!     |")
            print("|                                    See you at work!                                              |")
            print("+--------------------------------------------------------------------------------------------------+")
            print("\n")
            exit()

        elif confirm_or_not == "No":
            modify_roster()
            break

        else:
            print("Invalid input! Please try again.")


    


