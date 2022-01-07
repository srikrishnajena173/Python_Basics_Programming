# Range() is an in-built function in python and we used that mostly in for loops 

# It produce a sequence of interger from start to stop 
# Its create an object, with which we can iterate 

print(range(100)) # O/P :- range(0, 100)

# OR 

print(range(1, 23)) # O/P :- range(1, 23)

# Example 1 :-
for item in range(0,100):
    print(item) # O/P :- 0 1 2 3....99

for item in range(2,100):
    print(item) # O/P :- 2 3....99

for item in range(100):
    print(item) # O/P :- 0 1 2 3....99 , bydefualt its take the 0th the starting point

# Example 2 :-
for v in range(0,10,2):
    print(v) # O/P :- 0,2,4....10 , so its jump over the 2

# Example 3 :- 
for m in range(10, 0, -1):
    print(m) # O/P :- 10,9,8...1 , it runs a reverse loop

# Example 4 :- create multiple list using for range ()
for li in range(3):
    val = list(range(10))
    print(val)

# O/P :- 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]