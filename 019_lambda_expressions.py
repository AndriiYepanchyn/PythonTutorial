number_list = [1, 2, 3, 4, 5, 6]
s_list = ['hi', 'hello', 'alloha', 'Dear diary']

def get_square(num):
    return num * num

def is_a_in_string(string):
    if 'a' in string:
        return True
    else:
        return False

# # function map
# # map(function, args) is an example of transfer function as parameter
# # map returns mapped result of function run with args

# res = map(get_square, number_list)
# print(res) # returns address of map returned by get_square

# for item in res:
#     print(item) #print iterated items  
# print( list(map(get_square, number_list))) #convert map of results to list

# print(list(map(is_a_in_string, s_list))) 
    

# function filter (function ,iterable)
#  It's iterate iterable arg and return only that values for which function returns True
# filter also return list of values

# print(list(filter(is_a_in_string, s_list))) 

# def is_odd(num):
#     return num % 2 == 1

# print(list(filter(is_odd, number_list)))


# lambda expressions
# print( list(map(get_square, number_list)))

# Here we saved named function get_square to use it in map, 
# this may be replaced by lambda as follows

print( list(map(lambda num: num * num, number_list)))

print( list(filter(lambda s: 'a' in s, s_list)))

# name s in lambda and s in function should be the same
