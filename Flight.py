from Airport import*

#The Flight Class
class Flight:

    #constructor:
    def __init__(self, flight_no, origin, dest, dur):
        #it is important to note that origin and destination are airport objects
        if not (isinstance(origin, Airport) and isinstance(dest, Airport)):
            #raise exception
            raise TypeError("The origin and destination must be airport objects")
        self._flight_no = flight_no
        self._origin = origin
        self._dest = dest
        self._dur = dur

    #the string representation of the flight
    def __str__(self):
        #determine if domestic or international
        type_flight = ""
        if self.is_domestic():
            type_flight += "domestic"
        else:
            type_flight += "international"

        #return description
        return self._origin.get_city() + " to " + self._dest.get_city() + " (" + str(round(self._dur)) + "h" + ")" + " [" + type_flight + "]"

    #define equality by same origin and destination
    def __eq__(self, other):
        #check if other is actually a flight
        if isinstance(other, Flight):
            return self._origin == other._origin and self._dest == other._dest
        else:
            return False

    def __add__(self, conn_flight):
        #check if connecting flight is actually a flight
        if isinstance(conn_flight, Flight):
            #check if the destination of the flight is the same as the origin of connecting flight
            if self._dest == conn_flight._origin:
                #make a new flight describing the total trip
                total_flight = Flight(self._flight_no, self._origin, conn_flight._dest, self._dur + conn_flight._dur)
                return total_flight
            else:
                raise ValueError("These flights cannot be combined")
        else:
            raise TypeError("The connecting_flight must be a Flight object")

    #getters
    def get_flight_no(self):
        return self._flight_no

    def get_origin(self):
        return self._origin

    def get_destination(self):
        return self._dest

    def get_duration(self):
        return self._dur

    #method that determines if a flight is domestic
    def is_domestic(self):
        #if the start and end are in the same country
        if self._origin.get_country() == self._dest.get_country():
            #flight is domestic
            return True
        else:
            return False

    #setters
    def set_origin(self, new_origin):
        self._origin = new_origin

    def set_destination(self, new_destination):
        self._dest = new_destination
