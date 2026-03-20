nested_list = [[1,2,3], [5,6,7], [9,8,7,6,5]]
# print(len(nested_list))
# print(nested_list)
# print(nested_list[2]) #nested list with index 2

# print(nested_list[1][0]) #print 5

just_list = []

# for i in range(len(nested_list)): 
#     for j in range(len(nested_list[i])):
#         just_list.append(nested_list[i][j])
# print(just_list)

# for i in nested_list: # Here i is the separate inner list 
#     for j in i: #Here we iterate items from inner list i
#         just_list.append(j) #j is a separate item from inner list i
# print(just_list)

# Using list comprehension
[[just_list.append(item) for item in inner_list] for inner_list in nested_list]
print(just_list)

# just_list.append( may be replaced directly by function print 
# in this case each char will be printed separately

