# List comprehension
greeting = 'Hello world'

# #  through the cicle
# letter_list=[]
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)

# #  inner cicle
# list2=[letter for letter in greeting]
# print(list2)

# #  number list from string
# list3 =  [int(num) for num in '0493021']
# print(list3)

# #  Number list from range
# list4 = [num for num in range(0, 100, 11)]
# print(list4)

# modifying before insert in list

# list5 = [num**3 -1 for num in range(5)]
# print(list5) #print item^3 - 1

# insert using condition

# list6 = [2, 5, 2, 56,-4, 67, -2, 34, -67]
# # list of even bigger then 0
# list7 = [num for num in list6 if num > 0 and num % 2 == 1] # may be applied compicated condition
# print(list7)

# # conditional assignment
# list8 = ['+' if num >=0 else '-' for num in list6 ] 
# print(list8)


# greetings = ['hello', 'hi', 'hey', 'hola']
# second_letter = [val[1] for val in greetings]
# print(second_letter)

# sec_second_letter = []
# for val in greetings:
#     sec_second_letter.append(val[1])
# print(sec_second_letter)

digits = [1,2,3,4,5,6,7,8,9]
odd = [num  for num in digits if num % 2 == 0]
print(odd)

odd2 =[]
for val in digits:
    if val %2 == 0:
        odd2.append(val)
print(odd2)