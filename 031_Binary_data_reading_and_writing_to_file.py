a = 0b01100110 #Binary format 0bXXXXXXX where X = 0 or 1
b = 0x1254fa6b #Hexadecimal format 0xAAAA where a = 0-9, a-f

print('a = ', a)
print('b = ', b)
print('b in binary = ', format(b,'0>32b'))
# format method make right binary shift on 32 signs and return value in binary format

print("a as binary", format (a, '0>16b'))
print("a as binary with left shift", format (a, '0<4b'))
print("a as hex with left shift", format (a, '0<4x'))
print("a as hex with right shift", format (a, '0>4x'))


# Writing binary files
file_name = 'C:\\PythonProjects\\HelloWorld\\write__binary_text.txt'
binary_write_mode = 'bw'
binary_read_mode = 'br'




with open(file_name, binary_write_mode) as binary_file:
    for n in range(64):
        binary_file.write(bytes([n]))
        #bytes conversion is mandatory for binary data, otherwise it will return error
        # [n] is necessary it allows to write number as number, otherwise it will be represented as n times of 0


with open(file_name, binary_read_mode) as read_file:
    for t in read_file.read():
        print(str(t) , ' = ', format(t, '0>8b'))   
        
 