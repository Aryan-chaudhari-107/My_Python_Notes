
''' By using the super() function, you do not have to use the name of the parent 
element, it will automatically inherit the methods and properties from its parent. '''

class Person:
  def __init__(self, fname, lname):
    print("hello there!!")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname, age):
    super().__init__(fname, lname) # This will call Person __init__ Function
    self.age = age 

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "you are", self.age, "year old right?" )

x = Student("bunny", "chaudhari", 21)
x.welcome()