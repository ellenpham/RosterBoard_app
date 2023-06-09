import datetime
from common_functions import *

# Define the Item class that represents an item object
class Item:
    
    # Initialize an Item object from input parameters
    def __init__(self, day, shift, action):
        self.day = day
        self.shift = shift
        self.action = action
    
    # Initialize an Item object from an input string
    @classmethod
    def from_str(self, str_data):
        try:
            str = str_data[0]
            str = str[4:]
            str = str.split("/")
            date = int(str[0])
            month = int(str[1])
            year = int(str[2])
            day = datetime.date(year,month,date)
            shift = str_data[1]
            action = str_data[2]        
            item = Item(day, shift, action)
            return item
        except ValueError:
            invalid_input_message()
    
    # This is how the item is represented in string    
    def __str__(self):
        return f"{self.day}, {self.shift}, {self.action}"