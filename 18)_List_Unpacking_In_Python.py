##############################  List Unpacking  #################################
# Example 15 :- a list feature called ..list unpacking 
a,b,c = [1,2,3]
print(a)
print(b)
print(c) # as you can see the list values are assigned to a,b,c
# O/P :-
# 1
# 2
# 3

# OR
a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other) # so here you can the rest of the items stored in the other variable 
# O/P :-
# 1
# 2
# 3
# [4, 5, 6, 7, 8, 9]

# OR 
a,b,c, *other, last_value = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(last_value) # so here you can the rest of the items stored in the other variable and 
# in the last_value it stored the last index of the list
# O/P :-
# 1
# 2
# 3
# [4, 5, 6, 7, 8]
# 9

############################## END ####################################
