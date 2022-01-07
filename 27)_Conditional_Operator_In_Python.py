is_old = False
have_licence = False

if is_old:                             ## Here the condition is false , so move to the next condition
    print('Is old enough to drive')
elif have_licence:                     ## Here again the condition is false, so move to the next condition    
    print('Have a valid licence')
else:                                  ## This is default condition and this will get print 
    print('Not old enough to drive and dont have licence')        

# O/P :- Not old enough to drive and dont have licence

#=================================================================================================

# If else conditions in python, if the type is Dictionary then calculate the mean of the Dictionary 
# else calculate the mean of the List
def mean(myValue):
    if type(myValue) == dict:                      # if the type == dictionary
        mean = sum(myValue.values()) / len(myValue)
    elif type(myValue) == list:                    # else if the type == list
        mean = sum(myValue) / len(myValue)
    else:                                          
        mean = None                                # else mean value = None
    return mean    

# invoke the function as dict
print(mean({"Jim": 10.2, "Sam": 34.0, "Rav": 30} ))
# O/P :- 24.733333333333334

# invoke the function as list
print(mean([10.2, 34.0, 30]))
# O/P :- 24.733333333333334

# invoke the function passing a float value
print(mean(10.4))
# O/P :- None