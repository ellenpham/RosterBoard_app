import os
import re

from create_roster_function import create_roster

# Start the program with a welcome banner

print("+-----------*****-----------******----------*****----------*****----------*****----------*****----------*****-----------+")
print("|                                               WELCOME TO ROSTERBOARD                                                  |")
print("+                            A work scheduling platform for all rostered staff of NKG Corp.                             +")
print("|                        A centralized space to monitor your roster and put your schedule in place.                     |")
print("+------------*****-----------******----------*****----------*****----------*****----------*****----------*****----------+")
print("\n")
print("-------------------------------------------------------------------------------------------------------------------------")
print("Please note that every second Thursday, we will release a new request. Turn on the notification to receive the request.")
print("You are required to action your work schedule by 12pm on the Sunday of the same week.")
print("Please contact our HR department on 1300 123 456 if you have any questions.")
print("-------------------------------------------------------------------------------------------------------------------------")
print("\n")
print("Please hit Enter to move on to the the application instructions...")
input()

# Instructions
print("+------------+")
print("|INSTRUCTIONS|")
print("+------------+")
print("\n")
print("Once you Start the work schedule process, you will be prompted to action the below requests:")
print("- Create your roster for the following week.")
print("- Inform us your unavailability for the next ONE week after the following week.")
print("- Modify your schedule if needed.")
print("\n")
print("Are you ready to Start your work schedule? Please hit Enter to start...")
input()
os.system('clear')
print("-------------------------------------------------------------------------------------------------------------------------")

# Employee information

# Input name
while True: 
    #Check if the string has any characters from a to z lower case, and A to Z upper case:
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    user_first_name = re.findall(r"^[a-zA-Z]+$", first_name)
    user_last_name = re.findall(r"^[a-zA-Z]+$", last_name)

    if user_first_name and user_last_name:
        print(f'\nHello {first_name}, we hope you are doing good!')
        break
    else:
        print("Invalid input! Please try again.\n")

print("\n")
# Department selection
def department_choice():
    print("Please select your department:")
    print("[1] Enter 1 for Operation")
    print("[2] Enter 2 for Inventory")
    print("[3] Enter 3 for Distribution")

    while True:
        try:
            department = int(input("Please enter your selection: "))
        except ValueError:
            print("Invalid input! Please try again.\n")
            continue

        if department != 1 and department != 2 and department != 3:
            print("Sorry, your selection is not in the list.\n")
            continue
        else:
            break
    
    if department == 1: 
        print("Operation")
    
    elif department == 2:
        print ("Inventory")
    else:
        print("Distribution")

department_choice()

print("-------------------------------------------------------------------------------------------------------------------------")

print("Let's start scheduling! Hit Enter to begin...")
input()
os.system('clear')

# Main menu
# print("-------------")
# print("| MAIN MENU |")
# print("-------------")

# File handling
# Availablity, Completed
# Day 1, Added
# Day 2, Modified
file_name = "schedule_record.csv"

# Check if schedule_records.csv exists
try:
    roster_file = open(file_name, "r")
    roster_file.close()
    print("Record existed")

except FileNotFoundError as e:
    roster_file = open(file_name, "w")
    roster_file.write("Rostered days, Actions\n")
    roster_file.close()
    print("Record is not existed, create records")


def main_menu():
    print("+-------------+")
    print("|  HOME MENU  |")
    print("+-------------+")

    print("Please select your option: ")

    print("[1] Enter 1 to create your roster for the following week")
    print("[2] Enter 2 to add your unavailability for ONE week after the following week")
    print("[3] Enter 3 to view your work schedule")
    print("[4] Enter 4 to modify your work schedule")
    print("[5] Enter 5 to exit the program")
    menu_choice = input("Enter your selection: ")
    return menu_choice

user_menu_choice = str()

while user_menu_choice != "5":
    user_menu_choice = main_menu()

    if(user_menu_choice == "1"):
        create_roster(file_name)
    
    elif(user_menu_choice == "2"):
        print("Add your unavailability")
    
    elif(user_menu_choice == "3"):
        print("View roster")
    
    elif(user_menu_choice == "4"):
        print("Modify roster")
    
    elif(user_menu_choice == "5"):
        print("\n")
        print("+--------------------------------------------------------------------------------------------------+")
        print("| See you again! Make sure you action your work schedule before this Sunday to secure your roster. |")
        print("| Please contact our HR department on 1300 123 456 if you have any questions.                      |")
        print("+--------------------------------------------------------------------------------------------------+")
        print("\n")
        continue
    
    else:
        print("Invalid input! Please try again.")