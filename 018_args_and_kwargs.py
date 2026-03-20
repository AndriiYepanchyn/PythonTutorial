#  *args and **kwargs

# def percents(num1, num2):
#     return num1 * num2 * 0.1

# print(percents(10, 20)) #percents (10, 20, 30 ) return error because extra arg 30
 
# def printargs(*args):
#      print(type(args)) #return tuple of args
     
# printargs(10, 20, 30, 40)

# def multipercents(*args):
#     res = 1
#     for i in args:
#         res = res * i
#     return res*0.1

# print(multipercents(10,20,30,40))
# print(multipercents(10,20,30,40,50,60))


# def printargs(percents, *args): #position parameters should go first
#     res = 1
#     for i in args:
#         res = res * i
    
#     return res * percents

# print(printargs(15, 5, 20, 10, 6))

# **kwargs 
#  Mandatory requirement is the key word in pair key=value 
# should be text, not a number, boolean or other
# Positioning arg is allowed, but it always should be first
# If we use positioning parameter it's presents is mandatory

# def kwargs_func(**kwargs): #Allow use in args key: value pair
#     print(kwargs)
#     print(type(kwargs))
     

# kwargs_func(first = 1, second = 2, third = 3)

# def hello_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print( 'hello', kwargs['name'])
#     else:
#         print('hello unkown user')
        
# hello_kwargs(surname='Santa Klaus', age = 2000, marriage = 'divorsed')
# hello_kwargs(name='Santa Сlaus', age = 2000, marriage = 'divorsed')
  
 
 
#  *args and **kwargs in one place

# def mixed_func(*args, **kwargs):
#     print(type(args))
#     print(kwargs) 
    
# mixed_func('a' ,'b', 'c', 'd', a=67, b=68, c=69)  

# def unproper_mixed_func(**kwargs, *args):
#     print(type(kwargs))
#     print(args) 
    
# unproper_mixed_func(a=67, b=68, c=69, 'a' ,'b', 'c', 'd')  

# def is_cat_here(*args):
#     for word in args:
#         if str(word).lower() == 'cat':
#             return True
#     return False

# print(is_cat_here('dog', 'ant', 'cAt'))
# print(is_cat_here('dog', 'ant', 'cow'))


# def is_item_here(item = '', *args):
#     return item in args


# print(is_item_here('table', 'chair', 'sofa', 'wall'))
# print(is_item_here('table', 'chair', 'sofa', 'wall', 'table'))

def your_favorite_color(my_color, **kwargs):
    if('color' in kwargs.keys()):
       print('My favorite color is %s, but %s is also pretty good!'
             %(my_color, kwargs['color']))
    else: 
        print('My favorite color is %s, what is your favorite color?' %my_color)    
        
        
your_favorite_color('red', name = 'Alice', age=15, pet='mice')
your_favorite_color('red', name = 'Alice', age=15, pet='mice', color = 'yellow')