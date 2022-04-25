# COP2510 Assignment 7 Part 1
# Michael Alexander (U62660400)
# Driver: Michael
# Navigator: Kenny (U14837275)
# Participation: 50/50
# Description: This program creates a class for polygons that calculates the area and perimeter for any polygon with
# number of sides and length of each side.

import math

class RegularPolygon:

    def __init__(self):
        self.__number_sides = 0
        self.__length = 0.0

    def set_number_sides(self, number_sides):
        self.__number_sides = number_sides

    def set_length(self, length):
        self.__length = length

    def get_number_sides(self):
        return self.__number_sides

    def get_length(self):
        return self.__length

    def perimeter(self):
        return self.__length * self.__number_sides

    def area(self):
        return (self.__number_sides * (self.__length ** 2)) / (4 * math.tan(math.pi / self.__number_sides))

def main():
    polygon1 = RegularPolygon()
    number_sides = int(input('Enter the number of sides (>=3): '))
    while number_sides < 3:
        number_sides = int(input('Invalid entry. Re-enter the number of sides (>=3): '))
    polygon1.set_number_sides(number_sides)
    length = float(input('Enter the length of each sides (>=0.1): '))
    while length < 0.1:
        length = float(input('Invalid entry. Re-enter the length of each sides (>=0.1): '))
    polygon1.set_length(length)
    print(f'The polygon has {polygon1.get_number_sides()} sides. Each side is {polygon1.get_length()} units in length.')
    print('The perimeter of the polygon is {:.3f} units and its area is {:.3f} square '
          'units.'.format(polygon1.perimeter(), polygon1.area()))
    
main()
