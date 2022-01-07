# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# 1. Python Arithmetic Operators
# Operator	     Name	          Example	

# +	             Addition	      x + y	
# -	             Subtraction	  x - y	
# *	             Multiplication	  x * y	
# /	             Division	      x / y	
# %	             Modulus	      x % y	
# **	         Exponentiation	  x ** y	
# //	         Floor division	  x // y


# 2. Python Assignment Operators
# Operator	      Example	       Same As	

# =	              x = 5	           x = 5	
# +=	          x += 3	       x = x + 3	
# -=	          x -= 3	       x = x - 3	
# *=	          x *= 3	       x = x * 3	
# /=	          x /= 3	       x = x / 3	
# %=	          x %= 3	       x = x % 3	
# //=	          x //= 3	       x = x // 3	
# **=	          x **= 3	       x = x ** 3	
# &=	          x &= 3	       x = x & 3	
# |=	          x |= 3	       x = x | 3	
# ^=	          x ^= 3	       x = x ^ 3


# 3. Python Comparison Operators
# Operator	      Name	                     Example
# ==	          Equal	                     x == y	
# !=	          Not equal	                 x != y	
# >	              Greater than	             x > y	
# <	              Less than	                 x < y	
# >=	          Greater than or equal to	 x >= y	
# <=	          Less than or equal to	     x <= y


# 4. Python Logical Operators
# Operator	        Description	                       Example

# and 	            Returns True if                    x < 5 and  x < 10
#                   both statements are true	
	 
# or	            Returns True if                    x < 5 or x < 4
#                   one of the statements is true	
	
# not	            Reverse the result,                not(x < 5 and x < 10)
#                   returns False if the result is 
#                   true not


# 5. Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location. like pointing to 
# the same memory.

# Operator	        Description	                        Example

# is 	            Returns True if both                x is y
#                   variables are the same object
	
# is not	        Returns True if both 
#                   variables are not the same object   x is not y

# Example 1. :- 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# O/P :- True
# returns True because z is the same object as x and both were pointing to the same memory location.
# (it means both are pointing to the same reference address)

print(x is y)
# O/P :- False
# returns False because x is not the same object as y, even if they have the same content, as both 
# memory allocated locations are different.
# (it means both are not pointing to the same reference address)

print(x == y)
# O/P :- True
# to demonstrate the difference betweeen "is" and "==": 
# this comparison returns True because x is equal to y , here it compares the value, rather than the
# allocated memeory location which mean they dont comparing the pointing reference address  

# Example 2. :-
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# O/P :- True
# returns False because z is the same object as x and both are pointing to same allocated memory location.
# (which means both are pointing to the same reference address)

print(x is not y)
# O/P :- True
# returns True because x is not the same object as y, even if they have the same content, as both are 
# pointing to different allocated memory or different reference address 

print(x != y)
# O/P :- False
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
# so, here it compare the values and the values are same , so for != its return false 

# 6. Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	         Description	                    Example

# in 	             Returns True if a sequence         x in y
#                    with the specified value 
#                    is present in the object
		
# not in	         Returns True if a sequence         x not in y
#                    with the specified value 
#                    is not present in the object


# Example 1. :- 
x = ["apple", "banana"]
print("banana" in x)
# O/P :- True
# Returns True because a sequence with the value "banana" is in the list

# Example 2. :-
x = ["apple", "banana"]
print("banana" not in x)
# O/P :- False
# Returns False because a sequence with the value "banana" is in the list


# 7. Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:#

# Operator	  Name	            Description

# & 	      AND	            Sets each bit to 1 if both bits are 1
# |	          OR	            Sets each bit to 1 if one of two bits is 1
# ^	          XOR	            Sets each bit to 1 if only one of two bits is 1
# ~ 	      NOT	            Inverts all the bits
# <<	      Zero fill left    Shift left by pushing zeros in from the right and let the leftmost bits fall off
#             shift	       
# >>	      Signed right #
#             shift	            Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off