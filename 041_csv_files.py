import csv
from pathlib import Path
import os

sourcefile = Path(__file__).parent / "resources" / "sample_5x10.csv"
targetfile = Path(__file__).parent / "resources" / "csv_writer_sample.csv"
filename2 = "resources\\sample_5x10 semicresources\\sample_5x10.csvolon devided.csv"
mode ="r"

# Simple way

# with open(sourcefile, mode) as file:
#     for line in file:
#        print(line)

# =====  Reading CSV files  =======

# SCV reader
# Allow read lines as lists

# with open(sourcefile) as file:
#     csv_reader = csv.reader(file)
#     csv_reader.__next__() #Allow skip headings
#     for line in csv_reader: #line is the simple list
#         # Prints only rows without headings
#         print(line)


# with open(sourcefile) as file:
#     csv_reader = csv.reader(file)
#     data_list = list(csv_reader) #Return list of lists
#     print(data_list)   


# DictReader allow to address to the filds by their names

# with open(sourcefile) as file:
#     csv_reader = csv.DictReader(file)
#     for line in csv_reader: 
#         # returns orered dict in such order which was defined during creation
#         print(line.get("Column_3"))     

# Using another delimiter (;) in same way it works in the csv.reader

# with open(filename2) as file:
#     csv_reader = csv.DictReader(file, delimiter=';')
#     for line in csv_reader: 
#         # returns orered dict in such order which was defined during creation
#         print(line.get("Column_3"))   
  

# =====  Writing to CSV files  ======
# with open(filename2, 'w', newline='') as file: #newline='' allow avoid extra new line symbols
#     csv_writer = csv.writer(file, delimiter=';')
#     csv_writer.writerow(['Added_val_1_11', 'Added_value_2_11', 'Added_value_3_11', 'Added_value4_11', 'Added_value_5_11'])
#     csv_writer.writerow(['Added_val_1_12', 'Added_value_2_12', 'Added_value_3_12', 'Added_value4_12', 'Added_value_5_12'])
#     csv_writer.writerow(['Added_val_1_13', 'Added_value_2_13', 'Added_value_3_13', 'Added_value4_13', 'Added_value_5_13'])
#     csv_writer.writerow(['Added_val_1_14', 'Added_value_2_14', 'Added_value_3_14', 'Added_value4_14', 'Added_value_5_14'])
#     csv_writer.writerow(['Added_val_1_15', 'Added_value_2_15', 'Added_value_3_15', 'Added_value4_15', 'Added_value_5_15'])



# result ={}
# with open(sourcefile) as file:
#     csv_reader = csv.DictReader(file, delimiter=',') 
#     for line in csv_reader: 
#         result[line["Column_3"]] = line["Column_5"]

#     print(result)      

# with open(targetfile, 'w', newline='\n') as file: #newline='' allow avoid extra new line symbols
#     csv_writer = csv.writer(file, delimiter=';')
#     for k, v in result.items():
#         csv_writer.writerow([k, v])    


# with open(targetfile, 'w', newline='\n') as file: 
#     headers = ['column#1', 'column#2']
#     csv_writer = csv.DictWriter(file, 
#                                 delimiter=';',
#                                 fieldnames=headers)
    
#     csv_writer.writeheader()
#     csv_writer.writerow({'column#1':'Field_1_1',  'column#2': 'Field_2_1'})
#     csv_writer.writerow({'column#1': 'Field_1_2', 'column#2': 'Field_2_2'})
#     csv_writer.writerow({'column#1': 'Field_1_3', 'column#2': 'Field_2_3'})




# =====  HomeWork  =====
# def add_students(name, surname, age):
#     headers = ['Name', 'Surname', 'Age']
#     with open(targetfile, 'a', newline='\n') as file: 
#         csv_writer = csv.DictWriter(file, 
#                             delimiter=';',
#                             fieldnames=headers)
        
#         if os.path.getsize(targetfile) == 0:
#             csv_writer.writeheader()

#         csv_writer.writerow({'Name': name, 'Surname' : surname, 'Age' : age})


# add_students('name_1', 'surname_1', '20')        
# add_students('name_2', 'surname_2', '25')        
# add_students('name_3', 'surname_3', '30')   

def print_students():
    print('======  print students  =====')
    with open(targetfile, newline='', mode=mode) as file: 
            csv_reader = csv.DictReader(file, delimiter=';') 
            for line in csv_reader: 
                table_row = "\
                    {n1:s} | {n2:10s} | {n3:10s} | {n4:10s} | {n5:8s} | {n6:5.0f} |\
                    ".format(n1='Name: ', n2=line.get('column#1'), n3='; Surname: ', n4= line.get('column#2'), n5='; Age = ', n6 = float(line.get('column#3') or 0))
                print(table_row) 

print_students()                
