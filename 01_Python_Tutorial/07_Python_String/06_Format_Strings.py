
# >>>>> STRING FORMAT <<<<< # :
''' As we learned in the Python Variables chapter, 
we cannot combine strings and numbers like this: '''

age = 36
txt = "My name is John, I am " + age
print(txt) # Error in code

''' But we can combine strings and numbers by using 
f-strings or the format() method! '''



# >>>>> F-STRING <<<<< # :
age = 36
txt = f"My name is John, I am {age}" 
print(txt) # Output: My name is John, I am 36



# >>>>> FORMAT <<<<< # :
#1
txt = "My name is {}, i am {}".format("john", 36)
print (txt) # Output: My name is John, I am 36

#2
txt = "My name is {0}, i am {1}".format("john", 36)
print (txt) # Output: My name is John, I am 36

#3
txt = "My name is {1}, i am {0}".format("john", 36)
print (txt) # Output: My name is 36 , I am John
 


# >>>>> PLACEHOLDERS AND MODIFIERS <<<<< # :
''' A placeholder can contain variables, operations, functions, 
and modifiers to format the value. Example: '''

price = 59
txt = f"The price is {price} dollars"
print(txt) # Output: The price is 59 dollars

''' A placeholder can include a modifier to format the value. '''
''' A modifier is included by adding a colon : followed by a legal
formatting type, like .2f which means fixed point number with 2 decimals: '''

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # Output: The price is 59.00 dollars

''' A placeholder can contain Python code, like math operations: '''

txt = f"The price is {20 * 59} dollars"
print(txt) # Output: The price is 1180 dollars