# First lets explore the bin() methods/functions in python 

# Example 1:-  Its Convert integer to binary using bin
number = 5
print('The binary equivalent of 5 is:', bin(number))
# O/P :- The binary equivalent of 5 is: 0b101

# Example 2:- Its convert from binary to decimal/integer 
print(int('0b101', 2))
# O/P :- 5

# Example 3 :- 
class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def __index__(self):
        return self.apple + self.orange + self.grapes 
        # here its adding 1 + 2 + 2 = 5, so here 5 binary number is 0b101 
        
print('The binary equivalent of quantity is:', bin(Quantity()))

# O/P :- The binary equivalent of quantity is: 0b101

# Second lets explore the complex() methods/functions in python

# Python complex() function is used to convert numbers or string into a complex number.
# This method takes two optional parameters and returns a complex number.
# The first parameter is called a real and second as imaginary parts.
# NOTE : its Signature is , complex ([real[, imaginary]])

# Example 1 :- Python complex() function example with integer value
# Calling function  
a = complex(1) # Passing single parameter  
b = complex(1,2) # Passing both parameters  
# Displaying result  
print(a)  
print(b)  

# O/P :- 
# (1+0j)
# (1+2j)

# Example 2 :- # Python complex() function example with float value
# Calling function  
a = complex(1.5) # Passing single parameter  
b = complex(1.5,2.2) # Passing both parameters  
# Displaying result  
print(a)  
print(b) 

# O/P :- 
# (1.5+0j)
# (1.5+2.2j)

# Example 3:- # Python complex() function example with string value
# Calling function  
a = complex('1') # Passing single parameter  
b = complex('1.5')  
# Displaying result  
print(a)  
print(b) 

# O/P :-
# (1+0j)
# (1.5+0j)

# NOTE :- It allows only one string parameter. 
# If the first argument is a string type, it does not allow to pass the second argument.
# It generates an error if we pass the second parameter.