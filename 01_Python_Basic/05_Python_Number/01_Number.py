
# >>>>> THERE ARE 3 NUMERIC TYPES IN PYTHON <<<<< # :
x = 1    # int 
y = 2.8  # float
z = 1j   # complex

print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'complex'>



# >>>>> INT <<<<< # : 
x = 1
y = 35656222554887711
z = -3255522

print(type(x)) # Output: <class 'int'>
print(type(y)) # Output: <class 'int'>
print(type(z)) # Output: <class 'int'>



# >>>>> FLOAT <<<<< # :
x = 1.10
y = 1.0
z = -35.59

print(type(x)) # Output: <class 'float'>
print(type(y)) # Output: <class 'float'>
print(type(z)) # Output: <class 'float'>

'''(Float can also be scientific numbers 
with an "e" to indicate the power of 10.)'''
x = 35e3 # 35 * 10^3 = 35000.0
y = 12E4 # 12 * 10^4 = 120000.0
z = -87.7e100 # -87.7 * 10^100 

print(x) # Output: 35000.0
print(y) # Output: 120000.0
print(z) # Output: -8.77e+101



# >>>>> COMPLEX <<<<< # :
'''(Complex numbers are written with 
a "j" as the imaginary part.)'''

x = 3+5j
y = 5j
z = -5j

print((x)) # Output: (3+5j)
print(type(y)) # Output: <class 'complex'>
print(type(z)) # Output: <class 'complex'>

