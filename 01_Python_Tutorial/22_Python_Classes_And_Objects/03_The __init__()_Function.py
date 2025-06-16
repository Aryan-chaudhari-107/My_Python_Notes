
''' 
All classes have a function called __init__(), which is always executed when the class 
is being initiated.

Use the __init__() function to assign values to object properties, or other operations that 
are necessary to do when the object is being created:

__xyz__ this are DUNDER method '''



class Person:
  def __init__(self, name, age, schooling): # DUNDER mehatod which is automatically called (not for every dunder method)
    print("Let's start")
    self.name = name
    self.age = age
    self.schooling = schooling
    self.buses = 10 # THIS CALL DEFULT VALUE


p1 = Person("John", 36, "completed")
print(p1.name) # Output: John
print(p1.age) # Output: 36
print(p1.schooling) # Output: completed
print(p1.buses) # Output: 10



''' 
Note: The __init__() function is called automatically every time the class is being used to create a new object. 
'''

