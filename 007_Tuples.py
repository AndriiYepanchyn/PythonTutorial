# Tupple is immutable and it's very useful to store sensitive information

tuple_1 = 1,2,3 #May be defined without brackets, but its better to use breckets
tuple_2 =('one', 'two', 'three')
mixed_tuple = ('item', 2, 3.4, True)
print(tuple_1)
print(tuple_2)
print(mixed_tuple)

print(type(tuple_1)) #allow to check object's class
print(tuple_2[1])

# tuple_2[2]='four' #Once assigned can't be modifyed

quazi_edited_tuple = (tuple_2[0], tuple_2[1], tuple_2[-1], 'four')
print(quazi_edited_tuple)

x=y=z=12
print(x,y,z)

x,y,z = 10,12,14
print(x,y,z)

person_tuple = ('Vasia', 'Pupkin', 33)
first_name, last_name, age = person_tuple
print(first_name, last_name, age)


t1=1,3,1,4,1,6,1,3

print(t1.count(1))
print(t1.count(3))

print(t1.index(4))
print(t1.index(1,3))# search 1 from index 3

pc = 'core i5', 'nvidia 1680', '32Gb', '2Tb'

CPU,GPU,RAM,HDD = pc
print(CPU,GPU,RAM,HDD)
