#Sets - collect unique objects

# colors = {"red", "yellow", "green", "blue"}

# print(colors)

# empty_set = {} #Creates dict instead of set

# print(empty_set)
# print(type(empty_set)) 

# empty_set=set()
# print(empty_set)
# print(type(empty_set)) 

# numbers = [1,2,3,4,4,4,4]
# text = ('one', 'two', 'three')

# set_of_numbers = set(numbers) #Only unique items left
# print(set_of_numbers)

# set_of_text = set(text)
# set_of_text.add('four')
# set_of_text.add('four')#will be ignored as duplicate
# print(set_of_text)

# x = set_of_text.pop() #Removes random item with the last index, returns item
# print(set_of_text)

# set_of_text.remove('three') # Removes specified item, returns void, attemp to remove absent item returns error

# print(set_of_text)

# set_of_numbers.discard(3) 
# set_of_numbers.discard(5) #Attempt to remove absent item do nothing

# print(set_of_numbers)

# set_of_numbers.clear

# print(set_of_numbers)

# set_of_chars = set('Once we went to the store')
# print(set_of_chars)


my_set = set('Billy Jaine is my love')

print(my_set)