# Tuple is nothing but a immutable list , where you cannot change the assigend values 
# Remember , however the list is mutable, you can modify/update the list 

# Example 1.
my_tuple = ('a','b','c','d','e')
print(my_tuple[1]) # O/P :- b, it return the 1st index value

# my_tuple[0] = 'l'
# print(my_tuple) # TypeError: 'tuple' object does not support item assignment
# You cannot udpate the tuple value

# Example 2 :- Slicing a tuple which is same as list 
my_tuple_sli = ('a','b','c','d','e')
new_tuple = my_tuple_sli[1:4]
print(new_tuple)
# O/P :- ('b', 'c', 'd')

##############################  Tuple Unpacking  #################################
# Example 3 :- 
a,b,c, *other, last_value = (1,2,3,4,5,6,7,8,9)
print(a)
print(other)
print(last_value)
# O/P :- 
# 1
# [4, 5, 6, 7, 8]
# 9