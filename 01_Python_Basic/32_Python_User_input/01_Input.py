
# # >>>>> USER INPUT <<<<< # :
# ''' Ask for user input: '''

# print("Enter your name:")
# name = input()
# print(f"Hello {name}")

# ''' Python stops executing when it comes to the input() function,
# and continues when the user has given some input.'''



# # >>>>> USING PROMPT <<<<< # :
# ''' The Python input() function has a prompt parameter, which acts 
# as a message you can put in front of the user input, on the same line: '''

# name = input("Enter your name:")
# print(f"Hello {name}")



# # >>>>> MULTIPLE INPUTS <<<<< # :
# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")



# # >>>>> INPUT NUMBERS <<<<< # :
# ''' The input from the user is treated as a string. Even if, in the 
# example above, you can input a number, the Python interpreter will 
# still treat it as a string. '''

# ''' You can convert the input into a number with the float() function: '''
# import math
# x = input("Enter a num: ")

# y = math.sqrt(float(x))
# print(f"The square root of {x} is {y}")



# >>>>> VALIDATE INPUT <<<<< # :
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x)
    y = False # If x is true it will move to the y which breaks the loop, and if x is not num it will directely enter to the exept 
  except:
    print("Wrong input, please try again.") 

print("Thank you!")