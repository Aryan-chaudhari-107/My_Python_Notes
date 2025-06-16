
''' + operator '''
print(10 + 5) 

''' Python divides the operators in the following groups: '''


# >>>>> ARITHMATIC OPERATORS <<<<< # :
''' Arithmetic operators are used with numeric values 
to perform common mathematical operations '''

'''  
OPERATORS 	       NAME	            EXAMPLE
    +	         Addition	           x + y	
    -	         Subtraction	       x - y	
    *	         Multiplication	     x * y	
    /	         Division	           10 / 3  = 3.333333334	
    %	         Modulus	           x % y	
    **	       xponentiation	     2 ** 3  = 2 x 2 x 2 = 8	
    //	       Floor division	     10 // 3 = 3

'''



# >>>>> ASSIGNMENT OPERATORS <<<<< # :
''' Assignment operators are used to assign values to variables: '''

'''
OPERATORS	             EXAMPLE	          SAME AS
    =	                  x = 5	               x = 5	
   +=	                  x += 3	           x = x + 3	
   -=	                  x -= 3	           x = x - 3	
   *=	                  x *= 3	           x = x * 3	
   /=	                  x /= 3	           x = x / 3	
   %=	                  x %= 3	           x = x % 3	
   //=	                x //= 3	           x = x // 3	
   **=	                x **= 3	           x = x ** 3	
   &=(bitwise and)	    x &= 3	           x = x & 3	
   |=(bitwise or)	      x |= 3	           x = x | 3	
   ^=(bitwise xor)	    x ^= 3	           x = x ^ 3	
   >>=	                x >>= 3	           x = x >> 3	
   <<=	                x <<= 3	           x = x << 3	
   :=	                  print(x := 3)	     x = 3, print(x) 
'''



# >>>>> COMPARISON OPERATORS <<<<< # :
'''
OPERATORS	         NAME	                         EXAMPLE 
==	               Equal	                       x == y	
!=	               Not equal	                   x != y	
>	                 Greater than	                 x > y	
<	                 Less than	                   x < y	
>=	               Greater than or equal to      x >= y	
<=	               Less than or equal to	       x <= y
'''



# >>>>> LOGICAL OPERATORS <<<<< # :
''' Logical operators are used to combine conditional statements: '''

'''
OPRATORS 	          DESCRIPTION 	                                           EXAMPLE
  and 	    Returns True if both statements are true	                     x < 5 and  x < 10	
  or	      Returns True if one of the statements is true	                 x < 5 or x < 4	
  not	      Reverse the result, returns False if the result is true	       not(x < 5 and x < 10)
'''



# >>>>> IDENTITY OPERATORS <<<<< # :
''' Identity operators are used to compare the objects, not if they are equal, 
but if they are actually the same object, with the same memory location: '''

'''
OPERATORS              DESCRIPTION                                              EXAMPLE
is 	           Returns True if both variables are the same object	            x is y	
is not	       Returns True if both variables are not the same object	        x is not y
''' 



# >>>>> MEMBERSHIP OPERATORS <<<<< # :
''' Membership operators are used to test if a sequence is presented in an object: '''

''' 
OPERATORS              DESCRIPTION                                              EXAMPLE
in             Returns True if a sequence with the specified                    x in y
               value is present in the object
not in         Returns True if a sequence with the specified                    x not in y
               value is not present in the object
'''



# >>>>> BITWISE OPERATORS <<<<< # :
''' Bitwise operators are used to compare (binary) numbers: '''

'''
OPERATORS     NAME                    DESCRIPTION                                    EXAMPLE
   & 	      AND	           Sets each bit to 1 if both bits are 1	                   x & y	
   |	      OR	           Sets each bit to 1 if one of two bits is 1	               x | y	
   ^	      XOR	           Sets each bit to 1 if only one of two bits is 1	         x ^ y	
   ~	      NOT	           Inverts all the bits	                                     ~x	
   
   <<	      Zero fill      Shift left by pushing zeros in  
            left shift     from the right and let the leftmost bits fall off         x << 2	
                               
   >>	      Signed right   Shift right by pushing copies of the
            shift          leftmost bit in from the left, and let the 
                           rightmost bits fall off	                                 x >> 2
'''