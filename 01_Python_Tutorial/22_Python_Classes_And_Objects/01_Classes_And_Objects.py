
'''  
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

'''



class employee:                     # employee is class
  language = "python"
  salary = 1200000                  # these 2 are class attributes 

bunny = employee() # bunny is Object
print(bunny.language, bunny.salary) # Output: python 1200000

p1 = employee()
p1.name = "harry" # instance attribute
print(p1.name, p1.language, p1.salary)



''' The examples above are classes and objects in their simplest form,
and are not really useful in real life applications '''
