
''' 
Inheritance allows us to define a class that inherits all the methods and properties from another class.

>> Parent class is the class being inherited from, also called base class.

>> Child class is the class that inherits from another class, also called derived class
'''



# >>>>> CREATE A PARENT CLASS  <<<<< # :
''' Any class can be a parent class, so the syntax is the same as creating any other class: '''

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

p1 = person("bunny", 21)
p1.printname()



# >>>>> CREATE A CHILD CLASS <<<<< # :
''' To create a class that inherits the functionality from another class, send the parent class 
as a parameter when creating the child class: '''

class person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class student(person):
    pass

p1 = student("bunny", "chaudhari")
p1.printname()