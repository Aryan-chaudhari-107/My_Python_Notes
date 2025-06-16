
# >>>>> IF STATEMENT <<<<< # :
""" If statement: """
a = 33
b = 200
if b > a: # (True)
  print("b is greater than a") # Output: b is graten than a 


""" If statement, without indentation (will raise an error): """
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error



# >>>>> IF...ELIF STATEMENT <<<<< # :
''' The elif keyword is Python's way of saying "if the 
previous conditions were not true, then try this condition". '''

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") # Output: a and b are equal



# >>>>> IF...ELIF...ELSE STATEMENT <<<<< # :
''' The else keyword catches anything which isn't caught by the preceding conditions. '''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") # Output: a is greater than b


''' You can also have an else without the elif: '''
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") # Output: b is not greater than a