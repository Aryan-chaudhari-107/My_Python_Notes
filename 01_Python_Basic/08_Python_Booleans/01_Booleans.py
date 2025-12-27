
# >>>>> BOOLEANS VALUE <<<<< # :
""" Booleans represent one of two values: True or False """

''' When you compare two values, the expression is 
evaluated and Python returns the Boolean answer: '''

print(10 > 9) # Output: True
print(10 == 9) # Output: Flase
print(10 < 9) # Output: Flase

''' Print a message based on whether the condition is True or False: '''
a = 200
b = 33

if b > a:
  print("b is greater than a") 
else:
  print("b is not greater than a") # Output: b is not greater than a



# >>>>> EVALUATE VALUES AND VARIABLES <<<<< # :
''' The bool() function allows you to evaluate any value, 
and give you True or False in return, '''

''' Evaluate a string and a number: '''
print(bool("Hello")) # Output: True
print(bool(15)) # Output: True

''' Evaluate two variables: '''
x = "Hello"
y = 15

print(bool(x)) # Output: True
print(bool(y)) # Output: True



# >>>>> MOST VALUES ARE TRUE <<<<< # :
''' 
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones. 
'''
 
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) # All are True



# >>>>> SOME VALUES ARE FALSE <<<<< # :
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) # All are Flase

''' One more value, or object in this case, evaluates to False, and 
that is if you have an object that is made from a class 
with a __len__ function that returns 0 or False: '''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



# >>>>> FUNCTION CAN RETURN A BOOLEAN <<<<< # :
def myFunction() :
  return True

print(myFunction()) # Output: True


def myFunction() :
  return True

if myFunction():
  print("YES!") 
else:
  print("NO!") # Output: True

''' Python also has many built-in functions that return a boolean value, 
like the "isinstance() function", which can be used to determine 
if an object is of a certain data type: '''
x = 200
print(isinstance(x, int)) # Output: True