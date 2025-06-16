
# >>>>> ARBITRARY ARGUMENTS, *ARGS <<<<< # :
''' If the number of arguments is unknown, add a * before the parameter name: '''

''' This way the function will receive a tuple of arguments, and can 
access the items accordingly: '''

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") # Output: The youngest child is Linus

''' Arbitrary Arguments are often shortened to *args in Python documentations. '''



# >>>>> KEY ARGUMENTS <<<<< # :
def my_function(child1, child2, child3):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# Output: The youngest child is Linus



# >>>>> ARBITRARY KEYWORD ARGUMENTS, **KWARGS <<<<< # :
def my_function(**kid):
  print("The youngest child is " + kid["lname"])

my_function(fname = "bunny", lname = "aryan")
  