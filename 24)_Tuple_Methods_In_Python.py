
# Method	Description

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# Example 1 :- count() method
tuple_count = (9,1,2,3,4,5,6,7,8,9)
count_value = tuple_count.count(9)
print(count_value) # O/P :- 2 , how many 9's are there in the tuple 

print(type(count_value)) # O/P :- <class 'int'> , its always return integer value 


# Example 2 :- index() method
tuple_index = (1,2,3,4,5,6,7,8,9)
index_val = tuple_index.index(4)
print(index_val) # so its return the index value of 4, which is 3


# Example 3 :- len(), a in-built function of python , we can use to count the length/size of the tuple
tuple_len = len(tuple_index)
print(tuple_len) # O/P :- 9

