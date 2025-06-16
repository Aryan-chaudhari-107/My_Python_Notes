
''' Objects can also contain methods. Methods in objects are functions that belong to the object. '''

# >>>>> OBJECT METHOD <<<<< # :
class Person:
  name = "bunny"
  age = 21

  def myfunc(self): # Object Method 
    print(f"Hello my name is {self.name} and i am {self.age}")

p1 = Person()
p1.myfunc() # Output: Hello my name is bunny and i am 21


# >>>>> STATICMETHOD <<<<< # :
class person:
  name = "bunny"
  age = 21

  def myfunc1(self):
    print(f"hello my name is {self.name} and i am {self.age} ")

  @staticmethod # This is a decorater
  def myfunc2():
    print("we used @staticmethod so we dont need to use self.")

p1 = person()
p1.myfunc1()
p1.myfunc2()