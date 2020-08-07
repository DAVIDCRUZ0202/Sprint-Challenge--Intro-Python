# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    #This is the base class for all other classes   
    pass

class FlightVehicle(Vehicle):
    # This is a child class to the vehicle class.
    pass

class Starship(FlightVehicle):
    # This is a child class to the FlightVehicle class.
    pass

class Airplane(FlightVehicle):
    # This is child class to the FlightVehicle class.
    pass

class GroundVehicle(Vehicle):
    # This is a child class to the Vehicle class.
    pass

class Car(GroundVehicle):
    # Child class to GroundVehicle.
    pass

class Motorcycle(GroundVehicle):
    # Child class to GroundVehicle.
    pass

# Notes on Class Inheritance
# Classes will always follow a parent-child heirarchy. If a class is inheriting from a different class, it also
# inherits all aspects of the original parent class. This is an explanation for why the class Motorcycle would
# inherit all qualities of the GroundVehicle class as well as all quallities of the original parent class, Vehicle.