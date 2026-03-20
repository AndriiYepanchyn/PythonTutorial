# v = input('inter something: ')
# print('you entered: ' + v)

# FILE READING CONSISTS OF 3 STEPS
# 1. This read txt file from path
file_name = 'C:\\PythonProjects\\HelloWorld\\textfile.htm'
mode ='r' # - optioanl param may have the different options
# For more info read method manual

# loren_ipsum = open(file_name, mode) #This is opened resource

# 2. This allow to get characters from read var
# for c in loren_ipsum:
#     print(c) # This will add empty string because the method default params
    # To avoid this we should change EOL param for the method print
    #print(text, sep = '<custom_value>', end = '<custom_value>')
     
 #3. This closes the file, next operations returns IOException
# loren_ipsum.close()

# for line in loren_ipsum:
#     if 'lor' in line.lower():
#         print(line)
        
        
# loren_ipsum.close() #This is necessary command except the follofing construction


# with open(file_name, mode) as loren2: 
#     #This is analog of try with resources and allow skip close command
#     for line in loren2:
#         if 'exp' in line.lower():
#             print(line, end = "")


# with open(file_name, mode) as loren2: 
#     line = loren2.readline()
#     while (line):
#         print(line, end='')
#         line = loren2.readline()
        
        
# with open(file_name, mode) as loren2: 
#     lines = loren2.readlines()
#     for c in lines:
#         print(c, end='')
        
#     print('\n' + lines[-1])    

# readline () - read 1 line - the best option to read large files
# readlines - read all lines separately and returns the list of lines
# read - read whole file in 1 string
