# There are 4 types of scope from  narrower to wider: 
#  local, 
#  enclosed,
#  global,
#  built-in

# Set equal names to the variabales with different scopes is a bad prictice, 
# but it will works by the following rules
from math import pi
# Each narrower scope variable will shadowing the variable with wider scope
# in this case we importing built-in variable pi from the math class
# but it will shadowed by every narrower variabe.


# Global scope visible everywhere inside class
# pi = 'global level variable' 

def outer_function():
    pi='enclosed variable' #Enclosed scope - visible evereywhere inside the outer function
    
    def inner_function():
        # If this variable will be commented will be used 
        # enclosed variable or other with wider scope
        pi = 'local variable'  #local scope - visible only  inside the inner function
        
        # We can adress directly to enclosed or wider variable using nonlocal if there is now local variable defined
        # nonlocal pi
        # after nonlocal pi was defined pi ='new value' will be assign value to the enclosed variable
        
        # To addres to the global variable we should ues global
        # global pi
        # pi = 'new value' # try dont do such things
        # It is highly recomended do not change the variables using nonlocal or global
        # this may occure to the hard catched errors
        print('inner funtion scope: ', pi)
    
    print('outer function scope', pi)
    # call of inner function
    inner_function()

print('class level scope: ', pi) 
outer_function()

 
    