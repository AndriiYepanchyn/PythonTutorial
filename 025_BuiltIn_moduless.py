import random  #This imports whole module
from random import randrange  # this imports only one function

for i in range(5):
    print(random.randint(1, 11))
    print(str(randrange(1, 20, 1)) + '\n-------')
    
from random import shuffle as list_shuffle  # This imports function as alias


my_list = [1,2,3,4,5,6,7]

random.shuffle(my_list)
print(my_list)

list_shuffle(my_list)
print(my_list)


# --------- HomeWork -------------

import math

num = 123456789
num2 = 987

print(math.sqrt(num))
print("------------")
print(math.factorial(num2))
print("------------")
print(math.pow(876, 54))

