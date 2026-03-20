# Dictionary and set comprehension

# numbers_dict = {'first':1, 'second':2, 'third': 3 }
# dict1 = {key: val**3 for key, val in numbers_dict.items()}
# print(dict1)

numbers_list =[1,-2,3,-4,5,-6,7,-8,9]
# dict2 = {num: num**2 for num in numbers_list}
# print(dict2)

# dict3 = {num: num for num in numbers_list if num >4}
# print(dict3)

# dict4 = {num: '+' if num > 0 else '-' for num in numbers_list }
# print(dict4)


numbers_dict = {'first':1, 'second':2, 'third': 3 }
set1 = {val**3 for val in numbers_dict.values()}
print(set1)

