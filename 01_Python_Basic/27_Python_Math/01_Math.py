
''' Python has a set of built-in math functions, including an extensive math module, 
that allows you to perform mathematical tasks on numbers. '''


# >>>>> BUILT IN MATH FUNCTION <<<<< # :

''' The min() and max() functions can be used to find the lowest or highest value in an iterable: ''' 
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x) # Output: 5
print(y) # Output: 25


''' The abs() function returns the absolute (positive) value of the specified number: ''' 
x = abs(-7.25)
print(x) # Output: 7.25


''' The pow(x, y) function returns the value of x to the power of y (xy). '''
x = pow(4,5)
print(x) # Output: 1024



# >>>>> THE MATH MODULE <<<<< # :
''' When you have imported the math module, you can start using methods and 
constants of the module. '''


import math

x = math.sqrt(64) # return square root
print(x) # Output: 8.0

y = math.ceil(1.4) # rounds a num upward to its nearest integer
z = math.floor(1.4) # rounds a num downwards to its nearest integer

print(x) # Output: 2
print(y) # Output: 1

p = math.pi
print(x) # Output: 3.14