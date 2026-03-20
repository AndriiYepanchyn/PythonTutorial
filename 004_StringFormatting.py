# print(1+1)
# print ('1'+'1')
# # print(1 + '2') // unsupported operation
# print(str(1) + '2') 
# print(1 + int('2')) 

###################################################
# name = "Jack"
# age = 23
# name_and_age = "My name is {0}. I'm {1} years old".format(name, age)
# print(name_and_age)
# name_and_age = "My name is {}. I'm {} years old".format(name, age)
# print(name_and_age)

# week_days = "There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}"\
#     .format("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satturday")
# print(week_days)    
# week_days2 = "There are 7 days in a week: {mo}, {tue}, {wed}, {th}, {fr}, {sat}, {su}"\
#     .format(su="Sunday", mo="Monday", tue="Tuesday", wed= "Wednesday", th="Thursday", fr ="Friday", sat="Satturday")
# print(week_days2) 

# week_days3 = "There are 7 days in a week: {mo}, {mo}, {mo}, {mo}, {mo}, {fr}, {su}"\
#     .format(su="Sunday", mo="Monday", tue="Tuesday", wed= "Wednesday", th="Thursday", fr ="Friday", sat="Satturday")
# print(week_days3) 

# su="Sunday"
# mo="Monday"
# fr ="Friday"

# week_days4 = "There are 7 days in a week: {mo}, {mo}, {mo}, {mo}, {mo}, {fr}, {su}" #doesn't catch the names
# print(week_days4) 

##################################################################################

# float_res = 10

# print(float_res)
# print ("Number = {0:1.3f}".format(float_res))
# print ("Number = {0:6.2f}".format(float_res))
#################################################################################


name = "Jack"
age = 13
# name_and_age = f"My name is {name}. I'm {age} years old" #Since v3.6
# print(name_and_age)

print("My name is %s. I'm %3.2d years old" %(name, age)) #%d may be pointed without formatting digits 3.2

n1 = 12.34
n2 = 2.546
n3 = 34534.2
n4 = 15
n5 = 9000.90
n6 = 45.893
n7 =142.2566
n8 = 345.90

table = f"\
{n1:15.4f}   |{n2:15.4f}   |{n3:15.4f}   |{n4:15.4f}   |\n\
{n8:15.4f}   |{n7:15.4f}   |{n6:15.4f}   |{n5:15.4f}   |\n\
"
print(table)

# -----------------------------------------------------------
table = "\
{n1:15.4f}   |{n2:15.4f}   |{n3:15.4f}   |{n4:15.4f}   |\n\
{n8:15.4f}   |{n7:15.4f}   |{n6:15.4f}   |{n5:15.4f}   |\n\
".format(n1=n1, n2=n2, n3=n3, n4=n4, n5=n5, n6=n6, n7=n7, n8=n8)

print(table)

