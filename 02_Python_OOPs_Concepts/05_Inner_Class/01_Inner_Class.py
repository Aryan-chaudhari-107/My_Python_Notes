'''
An inner class is a class defined inside another class. 
The inner class can access the properties and methods of the outer class.
Inner classes are useful for grouping classes that are only used in one place, 
making your code more organized.
'''

# A Car has an Engine
# An Employee has an Address

#Basic Syntax:
class Outer:
    class Inner:
        pass

# Example of Inner Class
class Student:
    def __init__(self, name):
        self.name = name
        self.addr = self.Address()   # creating Inner class object

    def show(self):
        print("Student Name:", self.name)
        self.addr.show()

    class Address:
        def show(self):
            print("City: Ahmedabad")
            print("State: Gujarat")


s = Student("Bunny")
s.show()


