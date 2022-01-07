# Python List have multiple methods ..like belows

# Method	    Description

# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

# Lets explore some list methods

# Example 1 :- sort() list method
amazon_cart_s = [2,1,3,6,5,4]
amazon_cart_s.sort() # so here in this line it will sort the amazon_cart_s and update the value
print(amazon_cart_s)
# O/P :- [1, 2, 3, 4, 5, 6]

# Example 2 :- append() list method
amazon_cart_a = [1, 2, 3, 4, 5, 6]
amazon_cart_a.append(100) # so here it will add the new value i.e. 100 after the last index of list
print(amazon_cart_a)
# O/P :- [1, 2, 3, 4, 5, 6, 100]


# Example 3 :- insert() list method -----> insert(index, object)
amazon_cart_i = [1, 2, 3, 4, 5, 6]
amazon_cart_i.insert(2, 100) # we are inserting the value 100 in 2nd index
print(amazon_cart_i)
# O/P :- [1, 2, 100, 3, 4, 5, 6]

# Example 4 :- extend() list methods ------> extend([list1, list2, list3...])
amazon_cart_e = [1, 2, 3, 4, 5, 6]
amazon_cart_e.extend([101, 100]) # here it will modify the list by adding 101 and 100 value
print(amazon_cart_e)
# O/P :- [1, 2, 3, 4, 5, 6, 101, 100]

# Example 5 :- pop() list methods ---> remove a specific index of the list
amazon_cart_p =  [1, 2, 3, 4, 5, 6]
amazon_cart_p.pop() # so here if you dont provide the index value, then by defult the pop()
# method will remove the last index
print(amazon_cart_p)
# O/P :- [1, 2, 3, 4, 5]

removed_val = amazon_cart_p.pop(2) # so here it will remove the 2nd index value from the index
print(amazon_cart_p)
# O/P :- [1, 2, 4, 5]
# again pop remove the value, but it return the removed value
print('Pop removed value is ' + str(removed_val))
# O/P :- Pop removed value is 3

# Example 5 :- remove() list methods ----> remove a specific value
amazon_cart_r =  [1, 2, 3, 4, 5, 6]
amazon_cart_r.remove(2)
print(amazon_cart_r)
# O/P :- [1, 3, 4, 5, 6]

# NOTE :- Suppose the below example where it returns none that means its not retuning anything
# its basically as null
removed_val = amazon_cart_r.remove(3)
print(removed_val) # O/P :- None, its just remove the object/value from the. Its not returning anything


# Example 6 :- clear() list method---> to clean the complete list
amazon_cart_c =  [1, 2, 3, 4, 5, 6]
amazon_cart_c.clear()
print(amazon_cart_c)
# O/P :- []

# Example 7 :- index(indexvalue, startindex, endindex) list method
# --> this will return the index value of the object
amazon_cart_ind = ['a', 'b', 'c', 'd', 'e' ]
index_val = amazon_cart_ind.index('c', 1 , 5) # c = index value, 1 = start index, 5 = end index
# look the value 'c' in between the index 1 and 5 and return the index value
# and the return type will always be integer
print(index_val)
# O/P :- 2

# Example 8 :-
print('b' in amazon_cart_ind) # so 'in' is keyword in python look for that value is there inside the list
# O/P :- True

# Example 9 :- count() list method
amazon_cart_count = ['a', 'b', 'c', 'd', 'e' ]
print(amazon_cart_count.count('d'))
# O/P :- 1 , so here its looking for how many 'd' are present in the list


# Example 10 :- sort() list method --> sort the value provided
amazon_cart_sort =  ['a', 'c', 'e', 'd', 'e' ]
amazon_cart_sort.sort()
print(amazon_cart_sort)
# O/P :- ['a', 'c', 'd', 'e', 'e']

# NOTE :- Again we have a built-in function called sorted() in python
amazon_cart_sorted =  ['a', 'c', 'e', 'd', 'e' ]
sorted_value = sorted(amazon_cart_sorted)
# As its a function so we pass the value sorted(object)
# If it is a method, then it will object.sort()
print(sorted_value)
# O/P :- ['a', 'c', 'd', 'e', 'e']
print(amazon_cart_sorted)
# O/P :- ['a', 'c', 'e', 'd', 'e'] , so that mean the sorted function created a new list,
# it didnt change the existing list. However the sort() method change the existing list.
# And both are sorting the list

# Example 11 :- copy() list method
amazon_cart_copy =  ['a', 'c', 'e', 'd', 'e' ]
copy_value = amazon_cart_copy.copy()
print(copy_value + amazon_cart_copy )
# O/P :- ['a', 'c', 'e', 'd', 'e', 'a', 'c', 'e', 'd', 'e'] , so here it copied and add the list

# Example 12 :- revrese() list method
amazon_cart_reverse =  ['a', 'c', 'e', 'd', 'e' ]
amazon_cart_reverse.reverse()
print(amazon_cart_reverse)
# O/P :- ['e', 'd', 'e', 'c', 'a'], just reverse the value of the list

# OR :-

amazon_cart_reverse_1 =  ['a', 'c', 'e', 'd', 'e' ]
val_1 = amazon_cart_reverse_1[::-1]
print(val_1)
# O/P :- ['e', 'd', 'e', 'c', 'a'] # here it returns a new list object

print(amazon_cart_reverse_1)  # so as we can see the original value didnt changed
# O/P :- ['a', 'c', 'e', 'd', 'e']


# Example 13 :- range(start , end) or range(end) is a in-built functions of python
print(list(range(1, 50))) # so this will create the list from 1 till 49

# O/P :- 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
#  23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
#  43, 44, 45, 46, 47, 48, 49]

# Example 14 :- join(iterable) is string method --> iterable means any list objects
sentence = '$'
new_sent = sentence.join(['hi', 'how' , 'are', 'you'])
print(new_sent) # so here it joins the list of value with the sentence value 
# O/P :- hi$how$are$you

# OR 
new_sent_1 = '$'.join(['hi', 'how' , 'are', 'you'])
print(new_sent_1)
# O/P :- hi$how$are$you


