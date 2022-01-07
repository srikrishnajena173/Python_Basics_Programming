# List is a order sequence of objects (that can be any type :- int, str, float ..tuple, dic)

li1 = [1,2,3,4,5] # here its only integer
li2 = ['a', 'b', 'c', 'd', 'e'] # here its only string
li3 = ['a', 1 , True, 1.2] # here its string, integer, boolean and float

# List is a Data structure which means its way of organising the data's 
# Like you can manipulate the data as you want like removing the data , adding the data, 
# filtering some data.

# Example 1 :- 
amazon_cart = ['TV', 'Laptop']
print(amazon_cart[0])
# O/P :- TV

# print(amazon_cart[3]) # in this you will get an error
# IndexError: list 
# index out of range
# Which means the index range of the list is only 0-1, so its thrwoing the index out range error


# List Slice :- 
# In list slice is also same as string slice i.e. [start:stop:stepover], 
# it says from which index you want me to start and on which index you
# want me to stop. And stepover is how you want me to extract the value.

# Example 1 :- 
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[0:2]) # here it will consider 0 as 0th index and 2 as 2nd index
# O/P :- [0, 1]

# Example 2 :- 
print(my_list[2:]) # here it will consider 2 as 2nd index and till the last index.
# O/P :- [2, 3, 4, 5, 6, 7, 8, 9]

# Example 3 :- 
print(my_list[0:7:2]) # here it will consider 0 as 0th index, 7 as 7th index and step over with 2 values
# O/P :- [0, 2, 4, 6]

