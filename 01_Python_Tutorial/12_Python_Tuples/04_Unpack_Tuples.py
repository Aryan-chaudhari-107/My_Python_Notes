
# >>>>> UNPACKING A TUPLE <<<<< # :
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
# Output: apple
#         banana
#         cherry

''' Note: The number of variables must match the number of values 
in the tuple, if not, you must use an asterisk to collect the
remaining values as a list. '''



# >>>>> USING ASTERISK* <<<<< # :
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
# Output: apple
#         banana
#         ['cherry', 'strawberry', 'raspberry']


''' Add a list of values the "banana" variable: '''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow) 
print(red)
# Output: apple
#         ['banana', 'cherry', 'strawberry']
#         raspberry