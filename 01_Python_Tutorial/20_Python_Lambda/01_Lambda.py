
''' 
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression. 
'''



# >>>>> SYNTAX <<<<< # :
''' lambda arguments : expression '''

#1: Add 10 to argument a, and return the result:
add = lambda a : a + 10
print(add(5)) # Output: 15 (5 is value of 'a')

#2: Lambda functions can take any number of arguments:
mul = lambda a, b : a * b
print(mul(5, 6)) # Output: 30

#3:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # Output: 13



# >>>>> WHY USE LAMBDA FUNCTIONS? <<<<< # :
''' 
The power of lambda is better shown when you use them as an anonymous function inside 
another function.

Say you have a function definition that takes one argument, and that argument will 
be multiplied with an unknown number:
 '''

#1: Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11)) # Output: 22

#2: Use the same function definition to make a function that always triples the number you send in:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11)) # Output: 33

#3: Use the same function definition to make both functions, in the same program:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))



''' Note: Use lambda functions when an anonymous function is required for 
a short period of time. '''