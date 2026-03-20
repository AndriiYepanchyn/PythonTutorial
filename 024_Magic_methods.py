class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age  = age
    
    def __str__(self):
        return 'Name: ' + self.first_name + ' ' + self.last_name 

    def __len__(self):
        return self.age
    
    def __del__(self):
        print ("Person" + self.name + ' is deleted') #Add additional functionality for default del()


# jack = Person('Jack', 'White', 26)

# print(jack) #Return address of object jack while method str() is not overridden

# print(len([1,2,3,4,5,6])) #Returns length of the list
# print(len(jack)) #Return error while it is not overridden in class

# del(jack) # Removes object jack
# print(jack) #Return error after the jack was removed


#  Operations  +, -, *, / - are defined as methods 
#  __add__(self, other)
#  __sub__(self, other)
# __mul__(self, other)
# __true_div__(self, other)
# see additional info at docs.python.org 



# ---------- Homework ----------------

class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items
        
    def __str__(self):
        return 'Chain of ' + str(self.number_of_items) + ' items'
    
    def __len__(self):
        return self.number_of_items
    
    
small_chain = Chain(15)
print(small_chain)
print(len(small_chain))