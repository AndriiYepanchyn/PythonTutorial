# class Car:
#     wheel_number = 4
#     def __init__(self, name, color, year, isCrashed):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.isCrashed = isCrashed
#         print('Car is created')
        
#     def drive(self, city):
#         print(self.name + ' is driving to ' + city)
        
#     def change_color(self, color):
#         self.color = color
    
# class Truck(Car): # This means that Truck extends Car
#     # wheel_number = 6 #Here we redefine wheels_number for Truck class
 
#     # args list must be same as in extended class
#     def __init__(self, name, color, year, isCrashed):
#         Car.__init__(self, name, color, year, isCrashed)
#         print('Truck is created')
        
#         # Here we redefine nested method drive
#     def drive(self, city):
#         print("Truck " + self.name + ' is driving to ' + city)
    
#     # Define own method of the nested class 
#     def load_cargo(self, cargo):
#         print('Cargo loaded: ', cargo)
        
    
#     # Polymorphism
#     def change_color(self, color):
#         self.color = 'moody ' + color
    
    
    
    
    
       
        
# man_truck = Truck('Man', 'Orange', 2015, False)        
                    
# man_truck.drive('Toronto')  #Here we call nested method
# print('Man wheel number',  man_truck.wheel_number) #Here we call nested variable
# man_truck.wheel_number = 6 #Here we change nested variable
# print('Man wheel number', man_truck.wheel_number) 

# beatle = Car('Beatle', 'Green', 1968, False)

# print('Beatle wheel number',beatle.wheel_number)
# beatle.drive('Ottava')

# man_truck.change_color('Brown')
# car_list = [man_truck, beatle]
# for l in car_list:
#     print(l.name + ' has ' + l.color + ' color')




# # Abstract class реалізуються через модуль abc (Abstract Base Classes)
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name
     
#     #This is method which hould be implemented  in successor class with exception 
#     def speak(self):
#          raise NotImplementedError('Class successor must implement speak()')  
     
#     # Abstract method
#     @abstractmethod
#     def get_pow_count(self):
#         pass #Абстрактний метод, який повинен бути реалізований у підкласі
    
    
    
# Homework

class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level
        
    def speak(self):
        print('Hi, my name is %s' %(self.name))
        
class Villain(GameCharacter):
       def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level 
        
       def speak(self):
        print( 'Hi, my name is %s and I will kill you' %(self.name))
        
       def kill(self, gameCharacter):
           gameCharacter.health = 0
           print('Bang-bang, now you\'re dead') 
           
           
gameChar = GameCharacter('Rooky', 10, 1)
villain = Villain('Angry monster', 100, 5)

gameChar.speak()
print('gameChar.health = ' , str(gameChar.health))   
villain.speak()
villain.kill(gameChar)
print('gameChar.health = ' , str(gameChar.health))        