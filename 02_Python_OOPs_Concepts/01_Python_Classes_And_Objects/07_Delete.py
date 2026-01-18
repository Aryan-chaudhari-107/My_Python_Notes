
# >>>>> DELETE OBJECT PROPERTIES <<<<< # :
''' You can delete properties on objects by using the del keyword: '''
class person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name, "i am", self.age)

p1 = person("John", 36)
del p1.age
p1.myfunc() # Error: 'person' object has no attribute 'age'



# >>>>> DELETE OBJECT <<<<< # :
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1) # Error: 'p1' is not defined
