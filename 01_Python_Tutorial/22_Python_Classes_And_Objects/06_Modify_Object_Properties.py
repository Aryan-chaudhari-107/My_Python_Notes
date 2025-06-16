
''' Set the age of p1 to 40: '''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name,", i am", self.age)

p1 = Person("John", 36)
p1.age = 40
p1.myfunc() # Output: Hello my name is John , i am 40