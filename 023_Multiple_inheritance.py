# class Swimmable:
#     def __init__(self, name):
#         self.name = name
        
#     def greeting   (self):
#         print(f'Hello, my name is {self.name}. I can swim') 
        
#     def swim(self):
#         print(self.name + " start swiming")


# class Walkable:
#     def __init__(self, name):
#         self.name = name
        
#     def greeting   (self):
#         print(f'Hello, my name is {self.name}. I can walk') 
        
#     def walk(self):
#         print(self.name + " Start walk")    
        

# class Flyable:
#     def __init__(self, name):
#         self.name = name
        
#     def greeting   (self):
#         print(f'Hello, my name is {self.name}. I can fly') 
    
#     def fly(self):
#         print(self.name + " start fly")
  
# #   This class inherit multiple classes
# # The order of definition superclasses is matter for 
# class GameCharacter( Swimmable, Walkable,  Flyable):
#     def __init__(self, name):
#         self.name = name
#         Swimmable.__init__(self, name)
#         Walkable.__init__(self, name)
#         Flyable.__init__(self, name)
   
# #    If this method will be commented call of greeting wil call Swimable as first one declared superclass
     
#     def greeting   (self):
#         print(f'Hello, my name is {self.name}.')       

# james = Swimmable('James')
# james.greeting()


# peter = GameCharacter('Peter')
# peter.fly()
# peter.swim()
# peter.walk()


# print("James is walkable? " + str(isinstance(james, Walkable)))
# print("Peter is walkable? " + str(isinstance(peter, Walkable)))
# print("Peter is swimable? " + str(isinstance(peter, Swimmable)))
# print("Peter is flyable? " + str(isinstance(peter, Flyable)))
# print("Peter is object? " + str(isinstance(peter, object)))


# peter.greeting() #Execute greeting from Swimable because it defined first in GameCharacter

 
#  METHOD RESOLUTION ORDER
#       A
#      / \
#     B   C
#     \   /
#       D

class A:
    def do_something(self):
        print('Method from A')
        
class B(A):
    def do_something(self):
        print('Method from B')
        
class C(A):
    def do_something(self):
        print('Method from C')
        
class D (B, C):
    # def do_something(self):
    #     print('Method from D')
    pass
        
        
some_object = D()

some_object.do_something()


# if do_something in D is absent the following rule of method resolution will be applied

# How to know method reolution order (mro)?
# __mro__  - property
#  mro()   method
#  help()  method

print(D.__mro__)
print(D.mro())
print(help(D))

 

