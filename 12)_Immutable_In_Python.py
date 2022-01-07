# Important NOTE :- String are immutable in python, that means once you assign the value, 
# you cannot change or update the value.

# For Example 1 :- 
my_string_val = '0123456789'

# my_string_val[1] = '12' # so, here i want to change/update the 1st index of string value 
# and getting the below error.
# Error :- TypeError: 'str' object does not support item assignment

# The only way you can change/update the value if we re-assign the value again
my_string_val = '12Str'
print(my_string_val)

# NOTE :- So internally python remove all the old values ('0123456789') from the memory and 
# re-assign the new value i.e ('12Str') in that memory location.