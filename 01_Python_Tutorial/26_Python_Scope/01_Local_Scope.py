
''' 
A variable is only available from inside the region it is created. 
This is called scope. 
'''


# Local scope: 
''' A variable created inside a function belongs to the local scope 
of that function, and can only be used inside that function. '''

def myfunc():
  x = 300 
  print(x)

myfunc() # Output: 300


# Function Inside Function:
''' As explained in the example above, the variable x is not available 
outside the function, but it is available for any function inside the function: '''

def myfunc():
  x = 300 
  
  def innerfunc():
    print (x)
    innerfunc()

myfunc() # Output: 300