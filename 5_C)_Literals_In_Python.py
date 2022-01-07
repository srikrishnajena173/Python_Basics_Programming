
# Literal is a raw data given in a variable or constant.
#  In Python, there are various types of literals they are as follows

######################## 1. Numeric Literals ###############################
# Numeric Literals are immutable (unchangeable). 
# Numeric literals can belong to 3 different numerical types: Integer, Float, and Complex.

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# O/P :- 
# 10 100 200 300
# 10.5 150.0
# 3.14j 3.14 0.0

######################## 2. String literals  #########################

# A string literal is a sequence of characters surrounded by quotes. 
# We can use both single, double, or triple quotes for a string. 
# And, a character literal is a single character surrounded by single or double quotes.

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
# O/P :- 
# This is Python
# C
# This is a multiline string with more than one line code.
# Ünicöde
# raw \n string

################## 3. Boolean literals #############################

# A Boolean literal can have any of the two values: True or False.

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
# O/P :- 
# x is True
# y is False
# a: 5
# b: 10


####################### 4.Special literals  ########################
# Python contains one special literal i.e. None. We use it to specify that the field has not been created.
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

# Invoking methods
menu(drink)
menu(food)
# O/P :-
# Available
# None

######################## Literal Collections #############################
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

# O/P :- 
# ['apple', 'mango', 'orange']
# (1, 2, 3)
# {'a': 'apple', 'b': 'ball', 'c': 'cat'}
# {'o', 'a', 'e', 'i', 'u'}