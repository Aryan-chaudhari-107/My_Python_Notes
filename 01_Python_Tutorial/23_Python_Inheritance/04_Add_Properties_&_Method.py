
''' Add a property called graduationyear to the Student class: '''

class Person:
  def __init__(self, fname, lname):
    print("hello there!!")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname, clg):
    Person.__init__(self, fname, lname) # u can also use (Person.__init__(self, fname, lname))
    self.collage = clg # ADDED PROPERTIE
  
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the our college", self.collage) # ADDED METHOD

x = Student("bunny", "chaudhari", "ABC clg")
x.welcome()