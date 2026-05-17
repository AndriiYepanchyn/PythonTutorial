import csv

filename = "sample_5x10.csv"
mode ="r"

# Simple way
# with open(filename, mode) as file:
#     for line in file:
#        print(line)


# SCV reader
# Allow read lines as lists
# with open(filename) as file:
#     csv_reader = csv.reader(file)
#     csv_reader.__next__() #Allow skip headings
#     for line in csv_reader: #line is the simple list
#         # Prints only rows without headings
#         print(line)


# with open(filename) as file:
#     csv_reader = csv.reader(file)
#     data_list = list(csv_reader) #Return list of lists
#     print(data_list)   

with open(filename) as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader: 
        # returns orered dict in such order which was defined during creation
        print(line.get("Column_3"))     