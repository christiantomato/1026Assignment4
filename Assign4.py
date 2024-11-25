"""
Template for Assign4.py
Make sure to remove this comment and add a comment here as described in the assignment document.
Remove the pass keyword in each function once your implement it.
Don't forget that you also have to create the Flight.py and Airport.py files.
"""

from Flight import *
from Airport import *

#defining all the airports and flights containers as dictionaries
all_airports = {}
all_flights = {}

def load_data(airport_file, flight_file):
    #try to read in the data
    try:
        #open up the files
        airport_file = open(airport_file)
        flight_file = open(flight_file)

        #start with the airport file
        for line in airport_file:
            # split by the dash delimiter
            line = line.rsplit("-")
            # strip each part from trailing or leading whitespace, assign to appropriate variable
            code = line[0].strip()
            country = line[1].strip()
            city = line[2].strip()

            #create the airport object
            airport_object = Airport(code, city, country)
            #put it into the dictionary with the airport code as the key
            all_airports[code] = airport_object

        #read in flights file information
        for line in flight_file:
            #split by the dash delimiter, note that the 6 digit flight code has a hyphen
            line = line.rsplit("-", 3)
            #strip each part from trailing or leading whitespace, assign to appropriate variable
            flight_no = line[0].strip()
            origin_code = line[1].strip()
            destination_code = line[2].strip()
            duration = line[3].strip()

            #make the flight object - from the all_airports dictionary, get the actual airport object
            flight_object = Flight(flight_no, all_airports[origin_code], all_airports[destination_code], duration)

            #finally, add to the all_flights dictionary

            #if they key isn't in the dictionary
            if origin_code not in all_flights.keys():
                #add the flight to the dictionary, as a list
                all_flights[origin_code] = [flight_object]
            else:
                #append it instead if already exists
                all_flights[origin_code].append(flight_object)

        #return true if it was successful
        return True

    except Exception:
        #if there are any errors
        return False

def get_airport_by_code(code):
    pass


def find_all_city_flights(city):
    pass


def find_all_country_flights(country):
    pass


def find_flight_between(orig_airport, dest_airport):
    pass


def shortest_flight_from(orig_airport):
    pass


def find_return_flight(first_flight):
    pass


if __name__ == "__main__":
    # Add any of your own tests on your functions here.
    # Make sure you don't have any testing or debugging code outside of this block!
    load_data("airports.txt", "flights.txt")
    for each in all_airports.values():
        print(each)
    for each in all_flights.items():
        print(each)