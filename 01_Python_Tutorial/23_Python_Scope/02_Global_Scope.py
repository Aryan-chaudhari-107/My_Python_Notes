
''' A variable created in the main body of the Python code is a global 
variable and belongs to the global scope. '''


# Global Scoop: 
''' Global variables are available from within any scope, global and local. '''

x = 300 

def myfunc():
  print(x) 

myfunc() # Output: 300
print(x) # Output: 300
print("\n")


# Naming Variable:
''' If you operate with the same variable name inside and outside of a function, 
Python will treat them as two separate variables. '''

x = 300

def myfunc():
  x = 200
  print(x)

myfunc() # Output: 200
print(x) # Output: 300
print("\n")


# Global Keyword:
''' The global keyword makes the variable global. '''

def myfunc():
  global x
  x = 300
  print(x)

myfunc() # Output: 300
print(x) # Output: 300
print("\n")


''' Also, use the global keyword if you want to make 
a change to a global variable inside a function. '''
y = 300

def myfunc():
  global y
  y = 200
  print(y)

myfunc() # Output: 200
print(y) # Output: 200
