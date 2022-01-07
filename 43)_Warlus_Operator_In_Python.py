# Warlus Operator is assign as := , this operator is valid from pythoon 3.8 version and above
# Warlus operator can be use in only in the condition like if, while 
# Using this operator we store the value in a variable 

# Example 1 :-
my_string = 'Helloooo'
if ((my_variable := len(my_string)) > 4): # here in my_variable we are storing length of my_string 
    print(f'the string {my_variable} is too long')

# O/P :- the string 8 is too long

# Example 2 :- 
while((my_variable := len(my_string)) > 4):
    print(f'the string {my_variable} is too long')
    break

# O/P :- the string 8 is too long
