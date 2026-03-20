# range - returns range object
# general view range(start, end, increment)

def print_line():
    print("------------")

# for x in range(10):
#     print(x)

# for y in range(1, 20, 3):
#     print(y)
    
#to ger range as object
# print (range(5)) 

# convert to the list
# print (list(range(5)))

# get all indexes of the sequence

# my_string = 'Where is my socks?'
# letter_index = 0
# for letter in my_string:
#     print(str(letter)+ " is at index " + str(letter_index))
#     letter_index += 1 
# print_line()
   
# #returns tuple
# for item in enumerate(my_string):
#     print(str(item))
# print_line()
    
# # convert tuple to key and value
# for index, letter in enumerate(my_string):
#     print(str(letter)+ " is at index " + str(index))
# print_line()

# command in return true if value is in set (set in general sense)
# print("sign 'a' is in 'Jack': " , ('a' in 'Jack'))
list_of_n = [1,2,3,4,5,6,7]
# print ("8 is in list_of_n: ", 8 in list_of_n)        
     

# dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# print(2 in dict1)
# print(2 in dict1.keys())
# print('a' in dict1) #returns false because we should use value
# print('a' in dict1.values()) 

# print_line()

# Min and Max functions
# print(min(list_of_n))
# print(max(6,8,2))
# print(max('Hi my name Slim Shaggy'))
# print_line()

# Ascii code

# print(ord('A'))
# print(ord('a'))

# import library functions

# shuffle
from random import shuffle
shuffle(list_of_n) # void functions returns none
print(list_of_n)

# randint

from random import randint #randint(min, max) inncluding borders
print(randint(0, 20))