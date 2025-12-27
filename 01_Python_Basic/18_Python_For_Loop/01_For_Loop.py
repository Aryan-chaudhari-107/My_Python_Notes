
# >>>>> EXECUTE A SET OF STATEMENT <<<<< # :
''' A for loop is used for iterating over a sequence 
(that is either a list, a tuple, a dictionary, a set, or a string). '''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
# Output: apple
#         banana 
#         cherry



# >>>>> LOOPING THROUGH A STRING <<<<< # :
for x in "banana":
  print(x)



# >>>>> THE BREAK STATEMENT <<<<< # :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# Output: apple 
#         banana
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# Output: apple



# >>>>> THE CONTINUE STATEMENT <<<<< # :
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
# Output: apple
#         cherry



# >>>>> THE RANGE() FUNCTION <<<<< # :
''' The range() function returns a sequence of numbers, 
starting from 0 by default, and increments by 1 (by default), 
and ends at a specified number. '''

for x in range(6):
  print(x) 
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

''' Using the start parameter: '''
for x in range(2, 6):
  print(x) 

''' Increment the sequence with 3 (default is 1): '''
for x in range(2, 30, 3):
  print(x)



# >>>>> THE ELSE IN FOR LOOP <<<<< # :
for x in range(6):
  print(x)
else:
  print("Finally finished!")

''' Note: The else block will NOT be executed if the 
loop is stopped by a break statement. '''

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") # Output: 0 1 2



# >>>>> NESTED LOOP <<<<< # :
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
# Output: red apple
#         red banana
#         red cherry
#         big apple
#         big banana
#         big cherry
#         tasty apple
#         tasty banana
#         tasty cherry



# >>>>> THE PASS STATEMENT <<<<< # :
items = ["apple", "banana", "mango", "durian"]

for item in items:
    if item == "durian":
        pass  # We'll decide later what to do with durian
    else:
        print(f"Processing: {item}")