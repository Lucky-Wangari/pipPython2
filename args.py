# Write a function that takes an unknown number of arguments 
# and returns their sum.
def numbers(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

# Write a function that takes two arguments, the first being a 
# string and the second being an unknown number 
# of integers. The function should return a new string 
# where the integers have been added to the original string.
def numerals(input_string, *numbers):
    return(f"{input_string} {numbers}")

input_string = "This are the numbers"
numbers = [1,2,3,4,5]
new_string = numerals(input_string, numbers)
print(new_string)

# Write a function that takes an unknown number of keyword arguments 
# and returns
# a dictionary where the keys are the argument names 
# and the values are the argument values.
def information(**kwargs):
    return(kwargs)



# Write a function that takes an unknown number of keyword arguments, each with a 
# string value. The function should concatenate all the strings 
# and return the resulting string.
def figures(**kwargs):
    string1 = ""
    for kwarg in kwargs.values():
        string1 += kwarg
    return string1 
   
#Write a function that takes an unknown number of keyword arguments, each 
#with a string value. The function should concatenate all the strings and 
#return the resulting string.
def words(**kwargs):
    return " ".join(kwargs.values())



# Write a function that takes a list of integers and an unknown 
# number of additional integers as arguments. The function should 
# return the index of the first occurrence of the sum of 
# the list and the additional integers
    
def numbers(nums, *args):
   final = sum(nums) + sum(args)
   return final[0]
       
nums = [1,2,3,4,5]
nums2 = numbers(nums,)
print(nums2)

# Write a function that takes a function and an unknown number of arguments, 
# and returns the result of 
# calling the function with the arguments.
def details(function, **args):
    return(function, args)