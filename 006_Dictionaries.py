# # Dictionaries it's like  hashtables in java
# # Consist of immutable key and value
# car_prices = {'toyota': 6000, 'opel': 3000, 'bmw':8000 }
# print(car_prices)
# print(car_prices['toyota'])

# car_prices['mazda']=4000
# print(car_prices)

# car_prices['mazda']=2000 #replaces the value for the key
# print(car_prices)

# del car_prices['toyota']
# print(car_prices) #removes only 1 key

# car_prices.clear()
# print(car_prices) #Clear all key-values couples from car_prices

# del car_prices
# print(car_prices) #car_prices not defined error


# Key: value separates by :
# Pairs key1:value1, key2: value2 separates by comma ,
person = {
    'first_name': "Jack",
    'last_name': "Brown",
    'age': 33,
    "hobbies": ['football', 'sniping', 'photo'],
    'children': {'son': 'Mike', 'doughter': 'Alice'}
}

print('person: ',  person)
print("person's name: ", person['first_name'], " ", person['last_name'])
print("hoobies: ", person['hobbies'])
print("last hoobie: ", person['hobbies'][2])
print("person's childern: ", person['children'])
print("son: ", person['children']['son'])

person['car']='mazda'
print('person: ',  person)

print('person: keys',  person.keys())
print('person: values',  person.values())
print('person: items',  person.items())


# Create dict from keys and values
my_dict = dict.fromkeys((1, 2, 3, 4), ('one', 'two', 'three', 'four'))

print(my_dict)