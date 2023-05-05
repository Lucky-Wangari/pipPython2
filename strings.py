#  Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the 
# first two characters of each string

# Write a python function



def sentence(string1, string2):
    string1_swapped = string1[::3] + string2[::3]
    string2_swapped = string1[::3] + string2[::3]
    
    string3 = f"{string1_swapped} {string2_swapped}"
    return string3

string1 = "Today"
string2 = "rained"
final = sentence(string1,string2)
print(final)

# Write a Python function that takes a list of words
# and returns the longest word and the length of the longest one
def find_longest(words):
    length = 0
    longest = ""
    for x in words:
        if len(x) > length & len(x) > longest:
            return x
        
words = ["Today", "Monday","Thursday","December"]
sentence2 = find_longest(words)
            
        
# Write a Python function that takes two lists and returns
# True if they have at least one common member.
def common_numbers(listA, listB):
    for x in listA:
        if x in listB:
            return True
    
    return False

listA = [1,2,3,4,5]
listB = [1,2,3,4,5]
listC = common_numbers(listA, listB)
print(listC)
 

# Write a Python program to check whether all dictionaries 
# in a list are empty or not
def check_list(list_dicts):
    return(not dict for dict in list_dicts)

list_dicts = [{}, {}, {"name": "Lucky"}, {}]
list1 = check_list(list_dicts)
print(list1)
    
 
            
# Given a list of numbers, use list comprehension to remove
# all odd numbers from the list:
numbers = [3,5,45,97,32,22,10,19,39,43]

even_only = [x for x in numbers if x % 2 == 0]
print(even_only)



# Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5
for x in list_a:
    if x in list_b:
        print(x)
        
        
# Use a nested list comprehension to find all of the numbers from 
# 1-1000 that are divisible by any single digit besides 1 (2-9)
divisibility = [x for x in range(1, 1001) if(x in range(2, 10) % 2 == 0)]

print(divisibility)


# Write a Python function to remove all vowels in a string
def vowel_removal(sentence):
    new = ""
    vowels = "a", "e", "i", "o","u","A", "E", "I", "O","U"
    for x in sentence:
        if x in vowels:
            new += vowels
    return new
    
    
sentence = "Today is a friday morning"
sentence_1 = vowel_removal(sentence)
print(sentence_1)

#  Write a Python program that accepts a comma-separated 
# sequence of words as input and prints the distinct words 
# in sorted form (alphanumerically).
input_words = ["Today, has to be a god day, isn't it?"]
new_words = sorted(input_words)
print(new_words) 



