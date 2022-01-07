# NOTE :- Upper group has higher precedence than the lower ones. It is in descending order
# Operators	                                     Meaning

# ()	                                         Parentheses
# **	                                         Exponent
# +x, -x, ~x	                                 Unary plus, Unary minus, Bitwise NOT
# *, /, //, %	                                 Multiplication, Division, Floor division, Modulus
# +, -	                                         Addition, Subtraction
# <<, >>	                                     Bitwise shift operators
# &	                                             Bitwise AND
# ^	                                             Bitwise XOR
# |	                                             Bitwise OR
# ==, !=, >, >=, <, <=,                          is, is not, in, not in	Comparisons, Identity, Membership operators
# not	                                         Logical NOT
# and	                                         Logical AND
# or	                                         Logical OR

# Lets explore some examples 

# Example 1 :- 
print(10 - 4 * 2)
# O/P :- 2, So here Multiplication has higher precedence than substraction

# Example 2 :- 
print((10 - 4) * 2)
# O/P :- 12 , So here Parentheses () has higher precedence than multiplication

# Example 3 :- 
# Precedence of or & and
meal = "fruit"
money = 0

if meal == "fruit" or meal == "sandwich" and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")

# O/P :- Lunch being delivered, so here Precedence of 'and' is more than 'or'

# Example 4 :-
meal = "fruit"
money = 0

if (meal == "fruit" or meal == "sandwich") and money >= 2:
    print("Lunch being delivered")
else:
    print("Can't deliver lunch")

# O/P :- Can't deliver lunch, so here Parentheses () is precedence over the or