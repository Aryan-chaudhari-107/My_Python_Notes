
''' 
The self parameter is a reference to the current instance of the class, and
is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, but it
has to be the first parameter of any function in the class:
 '''

# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name, "and i am", abc.age)

p1 = Person("John", 36)

p1.myfunc() # Output: Hello my name is John and i am 36
