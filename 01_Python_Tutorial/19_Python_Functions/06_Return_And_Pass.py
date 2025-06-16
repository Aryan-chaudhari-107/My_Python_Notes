
# >>>>> RETURN VALUE <<<<< # :
#1
''' To let a function return a value, use the return statement: '''

def my_function(x):
  return 5 * x

print(my_function(3)) 
print(my_function(5))
print(my_function(9))

#2
def add(a, b):
    return a + b

result = add(5, 3)     # result = 8
print(result)          # Output: 8



# >>>>> THE PASS STATEMENT <<<<< # :
def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        pass  # Will handle zero later

check_number(0)
# Output: (No output, because pass is used when num == 0.)