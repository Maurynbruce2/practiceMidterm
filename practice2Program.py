import practice2Class as p
import csv
n = 0 



shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''


        
        

        

'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''


#open the csv file in read mode

infile = open('bookings.csv','r')

#create a csv object from the file object from the step above

csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

booked = {}

# use a for loop to iterate through each record in the bookings file
for x in shows: 
    if shows[x]['id'] == 9587:
        example = p.Play(shows[x]['id'],shows[x]['name'],int(shows[x]['capacity']),shows[x]['event_date'])
        for record in csvfile:
            booked1 = p.Booking(record[1],record[2])

            if record[0]==str(shows[x]['id']):
                if example.get_seats()<=0:
                    print('************** ERROR ****************')
                    print('Guest Name: ', booked1.get_customer_name())
                    print('Sorry, Show: ', example.get_name(), 'is sold out')
                    print('**************************************') 

                else:
                    example.seats_left(example.get_seats())
   

infile.close()
    


