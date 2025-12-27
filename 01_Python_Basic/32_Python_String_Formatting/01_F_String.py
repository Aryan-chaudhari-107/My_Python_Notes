
# >>>>> CREATING A STRING <<<<< # :
txt = f"The price is 49 dollars"
print(txt)



# >>>>> PLACEHOLDERS AND MODIFIERS <<<<< # :
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"  # Modifies .2f
print(txt)

txt = f"The price is {95:.2f} dollars" # Without keeping in variable
print(txt) 



# >>>>> PERFORM OPERATIONS IN F-STRINGS <<<<< # :
txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}" # if else inside placeholder
print(txt)



# >>>>> EXECUTE FUNCTION IN F-STRING <<<<< # :
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

''' you can create your own functions and use them: '''
def myconverter(x):
  return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude" # Feet into meter
print(txt)



# >>>>> MORE MODIFIERS <<<<< # :
price = 59000
txt = f"The price is {price:,} dollars" # Use a comma as a thousand separator:
print(txt)

""" Here is a list of all the formatting types. """
'''

  :<	    ::      	Left aligns the result (within the available space)
  :>	    ::      	Right aligns the result (within the available space)
  :^	    ::      	Center aligns the result (within the available space)
  :=	    ::      	Places the sign to the left most position
  :+	    ::      	Use a plus sign to indicate if the result is positive or negative
  :-	    ::      	Use a minus sign for negative values only
  : 	    ::      	Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
  :,	    ::      	Use a comma as a thousand separator
  :_	    ::      	Use a underscore as a thousand separator
  :b	    ::      	Binary format
  :c	    ::      	Converts the value into the corresponding Unicode character
  :d	    ::      	Decimal format
  :e	    ::      	Scientific format, with a lower case e
  :E	    ::      	Scientific format, with an upper case E
  :f	    ::      	Fix point number format
  :F	    ::      	Fix point number format, in uppercase format (show inf and nan as INF and NAN)
  :g	    ::      	General format
  :G	    ::      	General format (using a upper case E for scientific notations)
  :o	    ::      	Octal format
  :x	    ::      	Hex format, lower case
  :X	    ::      	Hex format, upper case
  :n	    ::      	Number format
  :%	    ::      	Percentage format
'''