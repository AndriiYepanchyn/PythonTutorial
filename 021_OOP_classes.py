# Defining new class:
# class ClassName:
#   static_class_member = value   #Define static variable

#   @classmethod                  # define static method
#   def get_static_method(cls)
#        do_something(cls)

#   @classmethod
#   def object_from_string(self, datastring):
#         arg1, arg2, ...argN = datastring.split(',')   # , is separator
#         new_object_name = cls('arg1', 'arg2', ...'argN' ) 
#         return new_object_name

#   def __init__(self, *args):     # define constructor
#       self.arg1 = arg1           # define object variable
#       self.argN = argN
#       self.synth_field = do_something(arg1, arg2) #define synthetic field
# 
#   def drive(self, args):          # define object method
#       do_something()
        
#   pass                           #This allow to create emty class


# Creating new object
#  new_object = ClassName(arg1 = 'arg1', arg2 = arg2, argN = argN)

# Access to the static member
#  ClassName.static_class_member
#  Classname.get_static_method()

# Access to the object related members
#  new_object.arg1
#  new_object.drive(self, args)


class MyClass:
    pass

new_object = MyClass()
print(type(new_object))

class Car:
    def __init__(self, name, color, year): # args sequence doesn't matter
        self.name = name
        self.color = color
        self.year = year
              
mazda = Car(name = 'Mazda RX', color = 'red', year = 2020);
print(mazda.name)

bmw = Car(name = 'BMW 760', year = 2021, color = 'black')
print(bmw.year)
 
# Static property

class NewCar:
    wheels = 4
    def __init__(self, name, color, year, isCrashed):
        self.name = name
        self.color = color
        self.year = year
        self.isCrashed = isCrashed
    def drive(self, city):
        print('Car', self.name, 'start driving to the', city)
        
    def change_color(self, new_color):
         self.color = new_color   

oldsmobil = NewCar('Oldsmobil', 'Biege', 1975, False)

print('oldsmobil.wheels = ', oldsmobil.wheels)
print('oldsmobil.year = ', oldsmobil.year)

cadilac = NewCar('cadilac', 'Biege', False, 2005) #We should be carefull creating objects in such way
# veriable types are not defined so we can get year = False

print('cadilac.wheels = ', cadilac.wheels)
print('cadilac.year = ', cadilac.year)

print('NewCar.wheels ', NewCar.wheels )
oldsmobil.drive('Alaska')

cadilac.change_color("Pink")

print('cadilac. new color =', cadilac.color)



class Circle:
    pi = 3.14
    def __init__(self, radius = 1): # Here we set default value for radius
        self.radius = radius
    
    def get_area(self):
        return self.radius ** 2 * self.pi    
    
    
circle1 = Circle(4)    
print('circle1.get_area() = ', circle1.get_area())   


# ==============================================================================
# Hometask 1
class BlogPost:
    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes
        
blogPost1 = BlogPost(user_name='John', text ='some text', number_of_likes= 5)        
blogPost2 = BlogPost(user_name='Janny', text ='some text', number_of_likes= 15)        
 
blogPost1.number_of_likes = blogPost1.number_of_likes + 1    

print('blogPost1.number_of_likes = ', blogPost1.number_of_likes)   
print('blogPost2.number_of_likes = ', blogPost2.number_of_likes)   

# Hometask 2

class BankAccount:
    def __init__(self, client_id, client_first_name, client_last_name, balance = 0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance
    
    def add(self, amount):
        self.balance = self.balance + amount #add amount state check
        
    def withdraw(self, amount):
        self.balance = self.balance - amount  #add amount state check