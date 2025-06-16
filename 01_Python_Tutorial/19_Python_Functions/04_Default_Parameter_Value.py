
''' If we call the function without argument, it uses the default value: '''

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India") 
my_function()
my_function("US")
# Output: I am from India
#         I am from Norway
#         I am from US



