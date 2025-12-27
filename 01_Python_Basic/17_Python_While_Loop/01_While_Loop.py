
# >>>>> WHILE LOOP SYNTAX <<<<< # :
''' With the while loop we can execute a set of statements 
as long as a condition is true. '''

i = 1
while i < 6: # This is a condition
  print(i)
  i += 1 # (i = i + 1) both are same
# Output: 1
#         2
#         3
#         4
#         5
print("\n")



# >>>>> THE BREAK STATEMENT <<<<< # :
''' With the break statement we can stop the loop even if the 
while condition is true: '''

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
# Output: 1
#         2
#         3
print("\n")



# >>>>> THE CONTINUE STATEMENT <<<<< # :
''' With the continue statement we can stop the current 
iteration, and continue with the next: '''

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("\n")



# >>>>> THE ELSE STATEMENT <<<<< # :
''' With the else statement we can run a block of code 
once when the condition no longer is true: '''

''' Print a message once the condition is false: '''

i = 1
while i < 6:
  print(i)
  i += 1
else:  
  print("i is no longer less than 6")
# Output: 1
#         2
#         3
#         4
#         5
# i is no longer less than 6
