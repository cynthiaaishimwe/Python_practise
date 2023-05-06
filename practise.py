#  1.Write a Python program to get a single string from two given strings, separated by a space, and 
# swap the first two characters of each string

def get_string(a, b):
    word1 = a[:2] + b[2:]
    word2 = b[:2] + a[2:]
    return word1+ " "+word2
print(get_string("cynthia","ishimwe"))

    
#  10.Write a Python function to remove all vowels in a string
def remove_vowels(name):
    vowels =('a','i','u','o','e')
    empty = " "
    for i in name:
        if i not in vowels:
            empty += i
    return empty
name = "beautiful"        
print(remove_vowels(name))

# 7. Given a list of numbers, use list comprehension to 
# remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]

def remove_odd_nums(numbers):
    
    newArray = [x for x in numbers if x%2 ==0]
    return newArray
numbers = [3,5,45,97,32,22,10,19,39,43]
print(remove_odd_nums(numbers))

#  4.Write a Python function that takes two lists and 
# returns True if they have at least one common member.

def common_members(a,b):
    
    for i in a:
        for x in b:
         if i ==x:
             return True
         else:
             False
            
             
a = [10,20,30,40,50]
b = [20,70,80,90,50]
print (common_members(a,b))

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)

def divisible_nums():
    newNums = [num for num in range(1, 1001) if (num % i == 0 for i in range(2, 10))]
    return newNums
print(divisible_nums())


# 5.Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"],
# ["#000000", "#FF0000", "#800000", "#FFFF00"]

def color_dictionary(a,b):
 a=["Black", "Red", "Maroon", "Yellow"]
 b=["#000000", "#FF0000", "#800000", "#FFFF00"]
list_of_dicts = dict(zip(a,b))
print(color_dictionary(a,b))

# Write a Python program to check whether all dictionaries in a list are empty or not

list1 = [{}, {}, {}]
list2 = [{}, {"key": "value"}, {}]

def dict(dict_list):
    return all(not d for d in dict_list)

print(dict(list1)) 
print(dict (list2)) 


# Write a Python program that accepts a comma-separated sequence of words as input
# and prints the distinct words in sorted form (alphanumerically).
def words (words):
    words_list = words.split(",")
    output = sorted(words_list)
    for i in output:
        print(i)

words("wel,helllo,my,name,hopper")






    

