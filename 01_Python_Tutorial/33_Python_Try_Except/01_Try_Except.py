
'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''



# >>>>> EXCEPTION HANDLING <<<<< # :
''' When an error occurs, or exception as we call it, Python will normally stop
and generate an error message. '''

''' These exceptions can be handled using the try statement: '''

try:
  print(x)
except:
  print("An exception occurred") # Output: An exception occurred



# >>>>> MANY EXCEPTION <<<<< # :
''' Print one message if the try block raises a "NameError" and another for other errors: '''

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong") # Output: Variable x is not defined



# >>>>> ELSE <<<<< # :
''' You can use the else keyword to define a block of code to be executed if no 
errors were raised: '''

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") # Output: Nothing went wrong



# >>>>> FINALLY <<<<< # :
''' The finally block, if specified, will be executed regardless if the try 
block raises an error or not. '''

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished") 
# Output: Something went wrong
#         The 'try except' is finished


''' This can be useful to close objects and clean up resources: '''
''' Try to open and write to a file that is not writable: '''

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")