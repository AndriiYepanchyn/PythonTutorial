number_list = [41, 12, 16, 18, 20.45]
print(number_list)
print(number_list[3])

dif_list=[23, 2.34, "do you like it?"]
print(dif_list)
print(dif_list[2])
# print(dif_list[3]) # Index out of bounds error

print(len(dif_list))
print(dif_list[1:3])

new_list = number_list + dif_list
print(new_list)

# dif_list[3] = "Yes"
# print(dif_list[3])

dif_list.append("Yes")
dif_list.insert(0, "numbers:") # 0 is item index

deleted = dif_list.pop(2) #2 - item index (-1) or () for last item

print(dif_list)
print("deleted: ", deleted)

print(number_list)
number_list.remove(20.45)
number_list += [89, 83, 16]

number_list.sort() #returns <None>
print(number_list)

# dif_list.sort() #Sort supported only for compatible types
# print(dif_list)

number_list.reverse()
print(number_list)

dif_list.reverse()
print(dif_list)

var = [89, 83, 41, 18, 16, 16, 12]
print(var)
new_var=[]
new_var.append(var.pop(1))
new_var.append(var.pop(1))
new_var.append(var.pop(1))
print(var)
print(new_var)
