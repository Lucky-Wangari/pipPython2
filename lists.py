# Write a Python program that takes a list of strings as input and
# outputs the number of times each string appears in the list, 
# using a dictionary and conditional statements.
def count(input_string):
    add = {}
    for x in input_string:
        if x in add:
            add += 1
            return add
        else:
            add = 1
            return add
        
input_string = ["Goodmorning", "find", "send", "fly"]
string1 = count(input_string) 
print(string1) 

# Write a Python program that takes a list of numbers as 
# input and outputs the median of the numbers 
def find_median(numbers):
    length = len(numbers)
    for x in numbers:
        if x % 2 == 0:
            middle = length / 2
            return middle
        else:
            return numbers
        
# Write a Python program that takes a list of numbers as input
# and outputs the second largest number in 
# the list using conditional statements and a for loop.  
def find_second(input_numbers):
   sort_nums = sorted(input_numbers)
   return sort_nums[-2]

input_numbers = [8,9,5,4,1,6,3]
new_nums = find_second(input_numbers)

# Write a Python program that takes a year as
# input and determines if it is a leap year.
def leep_year(year):
    if year % 4 == 0:
        return True
    elif:
    year % 4 != 0
    return False

year = 2023
if leep_year(year):
  print(f"{year} a leap year")
else:
    print(f"{year} is not a leap year")
    
#Write a Python program that takes a string as input and 
#checks if it is a palindrome (reads the same forwards and backwards), 
#ignoring spaces and punctuation.
def check_words(message):
    message = message.lower()
    message = message.replace(" ","")
    
    if message == message[::-1]:
        return True
    else:
        return False
    
    
    