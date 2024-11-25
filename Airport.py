"""
******************************
CS 1026 - Assignment 4 – Air Travel
Code by: Christian Tamayo
Student ID: ctamayo, 251433749
File created: Nov 25, 2024
******************************
This file contains the Airport class. It defines the
properties of our Airport data type, giving it values such as
code, city, and country. The Airport class also contains various
methods like equality, setters, and getters that allow us to manipulate
data.
"""

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
