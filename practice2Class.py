'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
class Play:
    def __init__(self,id,name,seats,date):
        self.__id = id 
        self.__name = name
        self.__seats = seats
        self.__date = date
        self.__status = 'True' 


    #create accessor methods for only name, seats, and status
    def get_name(self):
        return self.__name
    
    def get_seats(self):
        return self.__seats

    def get_status(self):
        return self.__status

    def set_seats(self,seats):
        self.__seats = seats 
    
    def seats_left(self,seats):
        self.__seats -=1 


    #Mutator Method 
    def set_status(self):
        self.__status = 'False'

class Booking:

    def __init__(self,customername,seat_number):
        self.__custname = customername
        self.__seatnumber = seat_number

    def get_customer_name(self):
        return self.__custname
    
    def get_seat_number(self):
        return self.__seatnumber
