

# Example 1
# Below is the code with example of while loop with User Input 
userName = ''

while userName != "pypy":
    userName = input("Enter user name: ")

# While loop ends when the condition is false

# While code example
a = 0
while a < 5:
    a = a + 1
    print(a)

#O/P :
# 1
# 2
# 3
# 4
# 5


# Exmaple 2, of While loop with break condition
while True:
    username = input("Enter username: ") ## input() a function where we provide the input in terminal 
    if username == "pypy":
        print("Breaking the while loop")
        break
    else:
        print("continue the while loop")
        continue 

# Example 3
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)

# Example 4
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
      offset = offset - 1
    else : 
      offset = offset + 1   
    print(offset)

