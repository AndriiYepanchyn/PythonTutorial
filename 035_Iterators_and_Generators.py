# 1. Ітератори (Iterator): це Об’єкт, який:
# має методи __iter__() і __next__(), повертає елементи по одному
# кидає StopIteration, коли дані закінчились

lst = [1, 2, 3] #List is iterable, so it may be iterated

# Default iterable types:
# list, tuple, range, str, bytes
# Datasets: set, frozenset, dict (by keys), 

it = iter(lst)   # отримали ітератор

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it) -> StopIteration

# list --------------------------
for x in [1, 2, 3]:
    print(x)
# tuple --------------------------
for x in (1, 2, 3):
    print(x)
# range --------------------------
for i in range(5):
    print(i)
# str --------------------------
for ch in "hello":
    print(ch)
# set --------------------------
for x in {1, 2, 3}:
    print(x)
# frozenset --------------------------
for x in frozenset([1, 2]):
    print(x)
# dict --------------------------
d = {"a": 1, "b": 2}

for k in d:
    print(k)  # a, b

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

# bytes -----------------------------
for b in b"abc":
    print(b)  # 97, 98, 99
# bytearray -----------------------------
for b in bytearray(b"abc"):
    print(b) 
# Files --------------------------
# with open("file.txt") as f:
#     for line in f:
#         print(line)
# Generators --------------------------
def gen():
    yield 1

for x in gen():
    print(x)

# NOT ITERABLE --------------------------
10        # int
3.14      # float
True      # bool
None

# iter(10) #Returns Type error object is not iterable

# How to check, does object iterable ---------
obj = []
from collections.abc import Iterable
print(isinstance(obj, Iterable))

# How to get type of Iterator -------------------------
# next(list_iterator) equeals list_iterator.__next__()
list_iterator = iter(lst)
print(type(list_iterator)) #<class 'list_iterator'>
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))

list_iterator = iter("Hello world")
print(type(list_iterator)) # <class 'str_ascii_iterator'>
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
print(list_iterator.__next__())
# print(list_iterator.__next__()) #StopIteration


def my_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            break

my_loop("New string")    

# Custom iterators  -------------------------------------

