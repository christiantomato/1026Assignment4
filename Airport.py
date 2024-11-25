#The Airport Class
class Airport:

    #constructor
    def __init__(self, code, city, country):
        self._code = code
        self._city = city
        self._country = country

    #the string representation of the object
    def __str__(self):
        return self._code + " (" + self._city + ", " + self._country + ")"

    #defining equality by having same flight code
    def __eq__(self, other):
        #check if other is actually an airport
        if isinstance(other, Airport):
            return self._code == other._code
        else:
            return False

    #getters
    def get_code(self):
        return self._code

    def get_city(self):
        return self._city

    def get_country(self):
        return self._country

    #setters
    def set_city(self, new_city):
        self._city = new_city

    def set_country(self, new_country):
        self._country = new_country

