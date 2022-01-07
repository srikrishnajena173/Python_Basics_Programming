# Lets explore the type conversion in python, so we convert int to string and vice-versa

# Example 1 :- Convert integer to string
integer_val = 100
string_val = str(integer_val)
print(type(string_val))
# O/P :- <class 'str'>

# OR 

print(type(str(100)))
# O/P :- <class 'str'>

# Example 2 :- Convert integer value to string value 
string_val1 = '100'
integer_val1 = int(string_val1)
print(type((integer_val1)))
# O/P :- <class 'int'>

# OR 

print(type(int(str(100))))
# O/P :- <class 'int'>

# Example 3 :-  Convert float to integer
print(type(int(float(10.2))))
# O/P :- <class 'int'>

# Example 4 :-  Convert integer to float
print(type(float(int(10))))
# O/P :- <class 'float'>

