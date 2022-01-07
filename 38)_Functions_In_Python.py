# So we will explore user defined functions, which we will going to create now

# def is short for define 
# function is useful if you want to use a code again and again 

# Example 1 :- 
def mean(myList):  ## mylist is a parameter of the function mean
    print("Starting of function mean()")
    mean = sum(myList) / len(myList)
    print("Ending of function mean()")
    return mean

# Invoking the mean method
print(mean([1, 2, 5]))    ## where as [1,2,5] are the actual argument of the function

val = mean([5, 6, 9])
print(val)

# So here mean() the a custome fuction created by us, however the sum() and len() are the inbuilt function of pyhton
print(type(mean), type(sum), type(len))
# O/P:- <class 'function'>   <class 'builtin_function_or_method'>  <class 'builtin_function_or_method'>


# Example 2 :- 
# In python we have something called None return type , examples
def myMean(myList):
    print("Starting of function myMean()")
    mean = sum(myList) / len(myList)
    print("Ending of function myMean()")
    return None 
   
myVal = mean([1, 28, 2])
print(myVal + 10)
