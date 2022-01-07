# Below are the escape characters used in Python:

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# Lets explore some 
# Example 1 :- 
txt = 'It\'s alright.'
print(txt) # so here to add the ' in between the It's we used a backward slash \

# Example 2 :- 
# path = 'C:\Users\Sri\Desktop\Python Doc.zip'
# print(path) # so here we are getting the below error
# Error :- SyntaxError: (unicode error) 'unicodeescape' 
# codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

# So now lets add the escape sequence
new_path = 'C:\\Users\\Sri\\Desktop\\Python Doc.zip'
print(new_path)
# O/P :- C:\Users\Sri\Desktop\Python Doc.zip

# Example 3 :- 
today_weather = 'It\'s a \"good weather\"'
print(today_weather)
# O/P :- It's a "good weather"