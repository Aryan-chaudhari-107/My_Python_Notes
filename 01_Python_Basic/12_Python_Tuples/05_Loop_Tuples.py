
# >>>>> LOOP THROUGH A TUPLE <<<<< # :
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
# Output: apple 
#         banana
#         cherry



# >>>>> LOOP THROUGH THE INDEX NUMBERS <<<<< # :
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
# Output: apple 
#         banana
#         cherry



# >>>>> USING WHILE LOOP <<<<< # :
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
# Output: apple 
#         banana
#         cherry



# >>>>> LOOPING USING TUPLE COMPREHENSION <<<<< # :
thistuple = ("apple", "banana", "cherry")
[print(x) for x in thistuple]
