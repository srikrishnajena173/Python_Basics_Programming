# NOTE :- Ternary Operator also called Conditional Expression
# From python 2.4 we got this Ternary Operator 

# Its a one-liner if else conditon 

# Example :- 1
is_your_friend = True
message = 'message the friend' if is_your_friend else 'dont message'
print(message) # O/P:- message the friend


is_your_friend = False
message = 'message the friend' if is_your_friend else 'dont message'
print(message) # O/P:- dont message


# Example :- 2
num1, num2 = 5, 10
min = num2 if num1 > num2 else num1
print(min) # O/P :- 5