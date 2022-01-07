# Simple Normal for loop with range value
for i in range(4):
    print(i+1) 

# O/P :- 
# 1
# 2
# 3
# 4   

# Below task is to print the round off value of the below list value using for loop
tmp = [9.1, 2.4, 23.9 , 34.2]

for t in tmp:
    print(round(t))

print("Done")
# O/P :- 
# 9
# 2
# 24
# 34
# Done


# Below task is to print only the integer value of the below list value using for loop
val = [10, 12, 9.1, 2.4, 23.9 , 34.2]
for intVal in val:
    if isinstance(intVal, int): # so if the value is instance of interger than only that value will print
        print(intVal)

# O/P :- 
# 10
# 12 

# Below task is to print the only the interget value and which is greater than 50
val1 = [12, 23.4, 23, 56, 78, 45.3]
for tmp in val1:
    if isinstance(tmp, int) and tmp > 50: # so if the value is instance of integer and greater than 50, then print
        print(tmp)

# O/P :- 
# 56
# 78  

# Example of nested for loop 
for x in [1,2,3,4]:
    for y in ['a', 'b', 'c', 'd']:
        print(x, y)

print('Done with nested loop')         



# ==================Some more examples of the for loop ==========================

# Suppose you want to iterate 2 values at time in the for loop 
mylistval = [12.1, 23.4, 34.5, 23.3, 23.2] 
for  index, val in enumerate(mylistval):
    print('index ' + str(index) + ': ' + str(val))

# O/P :- 
# index 0: 12.1
# index 1: 23.4
# index 2: 34.5
# index 3: 23.3
# index 4: 23.2


# Example 
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house:
    print("the " + x[0] + " is " + str(x[1]) + " sqm")

# NOTE:- [0] to access the name of the room and x[1] to access the corresponding area    