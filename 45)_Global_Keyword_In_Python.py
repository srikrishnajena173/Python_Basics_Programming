# Global is keyword in python is almost same as this keyword in Java.
# Global keyword we use to point global variable inside the local scope or function scope 

total = 0

def my_function_count():
    global total # --> here my local total variable is pointing to the global total, so intial value of total = 0
    total += 1
    return total

my_function_count()
my_function_count()
my_function_count()
print(my_function_count()) # O/P :- 4


# OR other way of doing this is 

total_1 = 0
def my_function_count_1(total_1):
    total_1 += 1
    return total_1
#
print(my_function_count_1(my_function_count_1(my_function_count_1(my_function_count_1(total_1))))) # O/P :- 4