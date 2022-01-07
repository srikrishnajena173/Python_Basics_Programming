# Method	                      Description

# add()	                          Adds an element to the set
# clear()	                      Removes all the elements from the set
# copy()	                      Returns a copy of the set
# difference()	                  Returns a set containing the difference between two or more sets
# difference_update()	          Removes the items in this set that are also included in another, specified set
# discard()	                      Remove the specified item
# intersection()	              Returns a set, that is the intersection of two or more sets
# intersection_update()	          Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                  Returns whether two sets have a intersection or not
# issubset()	                  Returns whether another set contains this set or not
# issuperset()	                  Returns whether this set contains another set or not
# pop()	                          Removes an element from the set
# remove()	                      Removes the specified element
# symmetric_difference()	      Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	  inserts the symmetric differences from this set and another
# union()	                      Return a set containing the union of sets
# update()	                      Update the set with another set, or any other iterable

# Example 1 :- add() methods  --> to add a value in sets
my_set_add = {'e', 'a', 'b', 'c', 'd', 'e'}
my_set_add.add('f') # it just the add the value, doesnt return anything
print(my_set_add) # O/P :- {'d', 'b', 'f', 'a', 'c', 'e'}

my_set_add.add('a')
print(my_set_add) # O/P :- {'c', 'f', 'b', 'a', 'd', 'e'} , here 'a' didnt added as 'a' is already there in the sets 

# Example 2 :- clear() method --> to clean the entire sets value 
my_set_clean = {'e', 'a', 'b', 'c', 'd', 'e'}
my_set_clean.clear()# it just the clean the sets, doesnt return anything
print(my_set_clean) # O/P :- set()

# Example 3 :- copy() method --> copy the unique values of the set
my_sets_copy = {'e', 'a', 'b', 'c', 'd', 'e'}
new_set_copy = my_sets_copy.copy()
print(new_set_copy) # O/P :- {'d', 'b', 'c', 'e', 'a'} , return the copy of a unique values from the old sets

# Example 4 :- difference() method
my_set_diff_1 = {1,2,3,4}
my_set_diff_2 = {3,4,5,6,7,8}
new_set_diff = my_set_diff_1.difference(my_set_diff_2)
print(new_set_diff) # O/P :- {1, 2}, so here it return the unique difference value
# between the 2 sets of 1st set
print(my_set_diff_1) # O/P :- {1, 2, 3, 4}, it didnt change the original value

# Example 5 :- discard() method
my_set_dis_1 = {1,2,3,4}
my_set_dis_2 = {3,4,5,6,7,8}
my_set_dis_1.discard(3)
print(my_set_dis_1) # O/P :- {1, 2, 4} , delete the provided value

# Example 6 :-   difference_update() method
my_set_diff_up_1 = {1,2,3,4}
my_set_diff_up_2 = {3,4,5,6,7,8}
my_set_diff_up = my_set_diff_up_1.difference_update(my_set_diff_up_2)
print(my_set_diff_up) # O/P :- None, it does not return anything, however it update the original values i.e.
print(my_set_diff_up_1) # O/P :- {1, 2}, so it remove the 1st set value which are present in the 2nd set
# and retun the unique values 

# Example 7 :- intersection() method
my_set_inter_1 = {1,2,3,4}
my_set_inter_2 = {3,4,5,6,7,8}
intersect_val = my_set_inter_1.intersection(my_set_diff_2)
print(intersect_val) # O/P :- {3, 4}, so it return the intersection/comman value between the 1st and 2nd sets
print(my_set_inter_1) # O/P :- {1, 2, 3, 4}, however it didnt updated/modify the 1st set value

# shortcut for intersection 
my_inte = my_set_inter_1 & my_set_diff_2
print(my_inte) # O/P :- {3, 4}

# Example 8 :- intersection_update() method
my_set_inter_up_1 = {1,2,3,4}
my_set_inter_up_2 = {3,4,5,6,7,8}
intersect_up_val = my_set_inter_up_1.intersection_update(my_set_inter_up_2)
print(intersect_up_val) # O/P :- None, so it does not return anything, however it update the
# intersection/comman value between the 1st and 2nd sets
print(my_set_inter_up_1) # O/P :- {3, 4},so it remove the 1st set value which are intersecting/comman 
# in the 2nd set and retun the unique values 


# Example 9 :- isdisjoint() method --> its validate do the both sets have any command/intersection point value 
my_set_isdisj_1 = {1,2,3,4}
my_set_isdisj_2 = {3,4,5,6,7,8}
print(my_set_isdisj_1.isdisjoint(my_set_isdisj_2))
# O/P :- False, as we have a command value between the sets i.e. 3 and 4

my_set_isdisj_3 = {1,2,}
my_set_isdisj_4 = {3,4,5,6,7,8}
print(my_set_isdisj_3.isdisjoint(my_set_isdisj_4))
# O/P :- True, as we dont have any command value between the 1st sets and 2nd sets

# Example 10 :- union() method --> unite/join/add both the sets , however remove the duplicates 
my_set_uni_1 = {1,2,3,4}
my_set_uni_2 = {3,4,5,6,7,8}
uni_val = my_set_uni_1.union(my_set_uni_2)
print(uni_val) # O/P :- {1, 2, 3, 4, 5, 6, 7, 8}
print(my_set_uni_1)
print(my_set_uni_2)
# O/P :- 
# {1, 2, 3, 4}
# {3, 4, 5, 6, 7, 8}, however it didnt modify the existing the sets

# shortcut for union
my_uni = my_set_uni_1 | my_set_uni_2
print(my_uni) # O/P :- {1, 2, 3, 4, 5, 6, 7, 8} 

# Example 11 :-  issubset()
my_set_subset_1 = {3,4}
my_set_subset_2 = {3,4,5,6,7,8}
print(my_set_subset_1.issubset(my_set_subset_2)) 
# O/P :- True, that mean i have the value in 1st set present in the 2nd set

my_set_subset_3 = {1,2,3,4}
my_set_subset_4 = {3,4,5,6,7,8}
print(my_set_subset_3.issubset(my_set_subset_4)) 
# O/P :- False, as i have 2 more values in 1st set i.e. 1 and 2 which is not present in the 2nd set

# Example 12 :-  issuperset()
my_set_superset_1 = {3,4}
my_set_superset_2 = {3,4,5,6,7,8}
print(my_set_superset_2.issuperset(my_set_superset_1)) # O/P :- True