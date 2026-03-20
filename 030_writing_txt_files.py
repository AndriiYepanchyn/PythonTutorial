colors = ['red', 'orange', 'yellow', 'blue', 'green', 'violet']
file_name = 'C:\\PythonProjects\\HelloWorld\\write_text.txt'
write_mode = 'w' # This tag rewrite existing file and replace all its data
append_mode = 'a' #this only append data to the existing file


with open (file_name, write_mode) as write_file:
    for color in colors:
        print(color, file=write_file)
        
        
text = open(file_name)   
for c in text:
    print(c.strip('\n')) # Strip cut tail part by the string defined as param not including it    
    
print('-'*40)    
    
with open (file_name, append_mode) as write_file:
    for color in colors:
        print('light ' + color , file=write_file)
        
text = open(file_name)   
for c in text:
    print(c.strip('\n')) # Strip cut tail part by the string defined as param not including it    