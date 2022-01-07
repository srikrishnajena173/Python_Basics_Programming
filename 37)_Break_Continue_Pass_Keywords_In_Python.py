# 1. Example of Break Keyword in python
my_list = [1,2,3,4]
for i in my_list:
    if i == 2:
        print(i)
        break  # O/P :- 2, so here it break the loop 


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break  # O/P :- 1 , so here it break the loop

# 2. Example of Continue Keyword in python
my_list1 = [1,2,3,4]
for i in my_list1:
    if len(my_list1) == 4:
        print(f'lenght value {len(my_list1)}')
        continue  # loop continue as the list length value is 4
    else:
        break 

# O/P :-  
#  lenght value 4
#  lenght value 4
#  lenght value 4
#  lenght value 4 , so here the loop continue as the list length value is 4


i = 0
while i < len(my_list1):
    print(my_list1[i])
    i += 1
    continue  # O/P :-1 2 3 4 , so here it continue with the loop 

# 3. Example of pass keyword in python
my_list1 = [1,2,3,4]
for i in my_list1:
    print(i)
    pass  # O/P :-1 2 3 4 , so here it pass the loop 


i = 0
while i < len(my_list1):
    print(my_list1[i])
    i += 1
    pass #  O/P :-1 2 3 4 , so here it pass the loop 
