# Lets first explore the Equal Equal '==' operator 

# NOTE 1 :- So,here the python first check the equallity in the 2 values
# NOTE 2 :- Then the Python internally check the type equality.

# Example 1 :- 
print(True == 1) 
# O/P :- True, 
print(bool(True)) # O/P :- True  
print(bool(1)) # O/P :- True and this is a type conversion as well
 # So now, True == True 

# Example 2 :- 
print('' == 1) # O/P :- False
# O/P :- False, so here the python check the equallity in the 2 values
# Python internally doing the below operation to check equality in the type
print(bool('')) # O/P :- False
print(bool(1)) # O/P :- True  
# So, now, False == True which is False

# Example 3 :- 
print(10 == 10.0) # O/P :- True
print(bool(10)) # O/P :- True  
print(bool(10.0)) # O/P :- True  
# So now, True == True

# Example 4 :- 
print(10 == 10.1) # O/P :- False
print(bool(10)) # O/P :- True  
print(bool(10.0)) # O/P :- True  
# here the first condition i.e. value equallity doesnt satisfy which is 10 is not equal to 10.1
# so , it doesnt matter if the type is equal

# Example 5 :- 
print([] == 1) # O/P :- False
print(bool([])) # O/P :- False 
print(bool(1)) # O/P :- True 
# So now, False == True which is false 

# Example 6 :- 
print([] == []) # O/P :- True
print(bool([])) # O/P :- False 
print(bool([])) # O/P :- False 
# So now, False == False which is False, however the both the values are same so its True
# 
# ########################################## is operator ######################################################

# So lets explore the 'is' operator 
# 'is' operator compares the memory location, if the both the values are pointing to the 
# same memory location,
# Its doesnt not compare the equality in the values 

# Example 1 :- 
print(True is True)
# O/P :- Ture , as both are pointing to the same memory location 

# Example 2 :- 
print('1' is '1')
# O/P :- Ture , as both are pointing to the same memory location 

# Example 3 :- 
print([] is [])
# O/P :- False , as both are not pointing to the same memory location,
# becasue when we create a new list it always allocate a memory location for that list 
# and when we create another list that will allocate an another memory location 

print([1,2,3] is [1,2,3]) # O/P :- False

# Example 4 :- 
b = []
a = [1,2,3,4]
a = b
print(a is b) # O/P :- True , as now 'b' list is point the 'a' list memory location 
