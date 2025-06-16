#1:
''' We want to add the __init__() function to the child class (instead of the pass keyword). '''

''' When you add the __init__() function, the child class will no longer inherit the 
parent's __init__() function. '''

class person:
  def __init__(self,first,last):
    self.firstname = first
    self.lastname = last

  def myfunc(self):
    print(self.firstname, self.lastname) 

class Student(person):
  def __init__(self, school):
    self.school = school

  def myfunc(self):
    print("school name is:", self.school)

x = Student("ABC School")
x.myfunc()


#2:
''' When you add the __init__() function, the child class will no longer inherit the 
parent's __init__() function. '''

''' To keep the inheritance of the parent's __init__() function, add a call to the 
parent's __init__() function: '''

class Person:
  def __init__(self, fname, lname):
    print("hello there!!")
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
  def __init__(self, fname, lname, age): 
    Person.__init__(self, fname, lname)
    self.age = age

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "you are", self.age, "old right?" )


x = Student("bunny", "chaudhari", 21)
x.welcome()