# >>>>> GLOBAL VARIABLE <<<<< # :
#1
x = "awesome" # global variable

def myfunc():
  print("Python is " + x)

myfunc() # Output: Python is awesome


#2
x = "awesome" # global variable
 
def myfunc():
  x = "fantastic" # local varibale
  print("Python is " + x)

myfunc() # Output: Python is fanstastic
print("Python is " + x) # Output: Python is awesome


# >>>>> THE GLOBAL KEYWORD <<<<< # :
#1
def myfunc():
  global x
  x = "fantastic" # This a global varibale now
  print("python is " + x)

myfunc() # Output: Python is fantastic
print("Python is " + x) # Output: Python is fantastic


#2
#changing the global variable 
x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("python is " + x)

myfunc() # Output: Python is fantastic
print("Python is " + x) # Output: Python is fantastic
