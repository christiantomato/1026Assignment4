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
            #split by the dash delimiter
            line = line.rsplit("-")
            #strip each part from trailing or leading whitespace, assign to appropriate variable
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
            #note that the duration is not a string
            duration = float(line[3].strip())

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
    #find the airport based on the given code by going through the dictionary
    for airport_code in all_airports.keys():
        if airport_code == code:
            #return the object if it exists
            return all_airports.get(code)
    #if we go through all airports and did not find an airport matching the code
    raise ValueError("No airport with the given code: " + code)

def find_all_city_flights(city):
    #find flights with either the origin or destination with the desired city
    city_flights = []

    #go through each list in the all_flights dictionary
    for flight_list in all_flights.values():
        #go through all the flights in each list
        for flight in flight_list:
            #if the flight origin or destination matches
            if flight.get_origin().get_city() == city or flight.get_destination().get_city() == city:
                #add it to the list
                city_flights.append(flight)

    return city_flights

def find_all_country_flights(country):
    #same as find_all_city_flights, except with country
    country_flights = []

    #go through each list in the all_flights dictionary
    for flight_list in all_flights.values():
        #go through all the flights in each list
        for flight in flight_list:
            #if the flight origin or destination matches
            if flight.get_origin().get_country() == country or flight.get_destination().get_country() == country:
                # add it to the list
                country_flights.append(flight)

    return country_flights

def find_flight_between(orig_airport, dest_airport):
    #is there a direct flight from the origin to destination?
    orig_airport_code = orig_airport.get_code()
    dest_airport_code = dest_airport.get_code()
    #this list is incase we need to look for a connecting flight later
    connecting_airport_candidates = []

    #go through the flight list in the dictionary with same origin airport
    #note that in the flights dictionary, not all origin airports show up as keys, so check for key error
    if orig_airport_code not in all_flights.keys():
        #raise the exception, there are no flights from this location
        raise ValueError("There are no direct or single-hop connecting flights from " + orig_airport_code + " to " + dest_airport_code)

    #proceed and check for direct flight
    for flight in all_flights[orig_airport_code]:
        #put the destination airport codes in the connection candidates
        connecting_airport_candidates.append(flight.get_destination().get_code())
        #check if any have the desired destination
        if flight.get_destination().get_code() == dest_airport_code:
            #then we have a match!
            return "Direct Flight: " + orig_airport_code + " to " + dest_airport_code

    #if we get to this point we need to find a "hop" connecting flight
    connections_set = set()
    for candidate_code in connecting_airport_candidates:
        #go through all the flights starting from the candidate
        #once again check if it is actually in the dictionary
        if candidate_code in all_flights.keys():
            #proceed
            for flight in all_flights[candidate_code]:
                if flight.get_destination().get_code() == dest_airport_code:
                    #then there is a possible connection and we can add it to the set
                    connections_set.add(candidate_code)

    #return the set if any possible connections were found
    if len(connections_set) > 0:
        return connections_set
    else:
        #nothing was found, this is so sad :(
        raise ValueError("There are no direct or single-hop connecting flights from " + orig_airport_code + " to " + dest_airport_code)

def shortest_flight_from(orig_airport):
    #go through all flights from the origin airport and find the lowest duration
    orig_airport_code = orig_airport.get_code()

    #set a sentinel value
    shortest_dur_flight = all_flights[orig_airport_code][0]
    #go through the list
    for flight in all_flights[orig_airport_code]:
        if flight.get_duration() < shortest_dur_flight.get_duration():
            #update the new shortest duration
            shortest_dur_flight = flight

    return shortest_dur_flight

def find_return_flight(first_flight):
    #find the reverse flight
    orig_airport_code = first_flight.get_origin().get_code()
    dest_airport_code = first_flight.get_destination().get_code()

    #go through all_flights and find the first flight from dest to orig
    for flight in all_flights[dest_airport_code]:
        if flight.get_destination().get_code() == orig_airport_code:
            #then we have found a return flight
            return flight

    #if we get to this point we did not find a return flight
    raise ValueError("There is no flight from " + dest_airport_code + " to " + orig_airport_code)

if __name__ == "__main__":
    # Add any of your own tests on your functions here.
    # Make sure you don't have any testing or debugging code outside of this block!

    #some tests :D
    load_data("airports.txt", "flights.txt")
    pearson = get_airport_by_code("YYZ")
    ohare = get_airport_by_code("ORD")
    edm = get_airport_by_code("YEG")
    bogota = get_airport_by_code("BOG")
    atlanta = get_airport_by_code("ATL")
    new_york = get_airport_by_code("JFK")
    denver = get_airport_by_code("DEN")
    mexico = get_airport_by_code("MEX")
    print(find_flight_between(edm, ohare))
    print(find_flight_between(edm, pearson))
    print(find_flight_between(ohare, mexico))
    print(find_flight_between(pearson, ohare))

