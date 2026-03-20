####################################################################
#   docs.python.org  contains docs about all built-in functions    #
####################################################################
# built-in functions
# x = print('xxx') # void function return NoneType
# y = set()

# print(type(x))
# print(type(y))

# built-in methods (methods is the functions of the objects)
# my_lyst = [1,2,3,4]
# my_lyst.append(6)
# print(my_lyst)
# my_lyst.clear()
# print(my_lyst)


# User defined function
# void functions
# Don't forget to add doc
# def printHello(name):
#     '''
#     :prints "Hello, 'name'" 
#     :param name - string to be concatanated and printed
#     :return None
#     '''
#     print('Hello,',name)
    
# printHello('dear user')

# # printHello() # returns Error TypeError missing 1 required arg
# # To avoid this error we should set default value


# def print_Hello_with_default(name = 'unknown person'):
#     print('Hello,', name)

# print_Hello_with_default('dear user')
# print_Hello_with_default()

# # functions with returned type

# # Don't forget to add doc
# def my_sum_of_three(a =0, b = 0, c =0):
#     '''
#     :args - a, b, c numbers to get their sum
#     :return - sum of the args
#     '''
#     return a+b+c
# print('5 + 6 + 7 = ', my_sum_of_three(5,6,7))

# print('sum_of_three(2, 3)  = ',  my_sum_of_three(2,3))

# y = my_sum_of_three(1, 2, 3)
# print('1 + 2 + 3 = ', y)

# help(my_sum_of_three) #print doc of the function

 
# def is_contains(string ='', val = ''):
#     if(val.lower() in string.lower()):
#         return True
#     else: return False


# bigStr = 'Hello my dear friend, hope all going well'
# search_str = 'friend'

# print('"', bigStr, '" contains "', search_str, '"? ', is_contains(bigStr, search_str) )

# # Simplifying function
# def is_contains2(string ='', val = ''):
#     return (val.lower() in string.lower())

# print('"', bigStr, '" contains "', search_str.upper(), '"? ', is_contains2(bigStr, search_str.upper()) )

# def cat_voice():
#     print("Meow!"*2)
    
# def dog_voice():
#     print("Woof!"*2)  
    
# cat_voice()
# dog_voice()

# def get_voice(text):
#     print(text,'!')
    
# get_voice('Hello, world')    

def odd_numbers(start = 0, end = 0):
    result = []
    if(end > start):
        if(start % 2 == 1):
            min = start
        else:
            min= start + 1
        
        for i in  range(min, end, 2):
            result.append(i)
    
    return result            
        
print(odd_numbers(3, 21))        