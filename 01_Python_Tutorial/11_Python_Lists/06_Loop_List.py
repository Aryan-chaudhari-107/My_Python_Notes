
# >>>>> LOOP THROUGH A LIST <<<<< # :
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
# Output: apple 
#         banana
#         cherry



# >>>>> LOOP THROUGH THE INDEX NUMBERS <<<<< # :
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
# Output: apple 
#         banana
#         cherry



# >>>>> USING WHILE LOOP <<<<< # :
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print (thislist[i])
  i += 1
# Output: apple 
#         banana
#         cherry



# >>>>> LOOPING USING LIST COMPREHENSION <<<<< # :
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
