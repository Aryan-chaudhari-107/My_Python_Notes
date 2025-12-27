
# >>>>> PARAMETERS OR ARGUMENTS? <<<<< # :
''' The terms parameter and argument can be used for the same 
thing: information that are passed into a function. '''

""" 
From a function's perspective: 

> Parameters = variable in the function definition. 
> Arguments = value passed when calling th function.
"""



# >>>>> ARGUMENTS <<<<< # :
''' Arguments are specified after the function name, inside the parentheses. 
You can add as many arguments as you want, just separate them with a comma. '''


def my_function(fname): # 'fname' is parameter
  print(fname + " Chaudhari")

my_function("Aryan") # 'Aryan' is argument
my_function("Bunny")
my_function("Herry")
# Output: Aryan Chaudhari
#         Bunny Chaudhari
#         Herry Chaudhari

''' Arguments are often shortened to "args" in Python documentations. '''



# >>>>> NUMBER OF ARGUMENTS <<<<< # :
''' By default, a function must be called with the correct number of arguments. Meaning 
that if your function expects 2 arguments, you have to call the function with 2 arguments, 
not more, and not less. '''

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Aryan", "Chaudhari")
my_function("Bunny", "patel")

''' If you try to call the function with 1 or 3 arguments, you will get an error: '''

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") # Error



