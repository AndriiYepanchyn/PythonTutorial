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
class Counter:
    def __init__(self, max_val):
        self.max = max_val
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

for x in Counter(3):
    print('private iterator', x)  # 1 2 3


# ------  GENERATORS  -------------------- 
# Генератори (Generator) 
# Це спрощений спосіб створення ітератора через yield.

# не потрібно писати __next__
# зберігає стан між викликами
# лінива (lazy) генерація
def gen():
    yield 1
    yield 2
    yield 3

g = gen()

print('Generator next = ', next(g))  # 
print('Generator next = ', next(g))  # 
print('Generator next = ', g.__next__())  # 
# print('Generator next = ', next(g))  # StopIteration

# Генератор у циклі
for x in gen():
    print(x)

# ----- Generator expression (аналог list comprehension)

g = (x * x for x in range(5))
print(next(g))  # 0   

# ---------------------------------------------------
# 1. Генерація великих даних (економія пам’яті)
# def read_large_file(file):
#     with open(file) as f:
#         for line in f:
#             yield line

# for line in read_large_file("big.txt"):
#     process(line)

#  Не вантажить файл у пам’ять

# ------------------------------------------------------
# 2. Пайплайни обробки даних
# def numbers():
#     for i in range(10):
#         yield i

# def squares(nums):
#     for n in nums:
#         yield n * n

# def even(nums):
#     for n in nums:
#         if n % 2 == 0:
#             yield n

# pipeline = even(squares(numbers()))

# print(list(pipeline))  # [0, 4, 16, 36, 64]

#  Ланцюжок обробки без проміжних списків
# ------------------------------------------------------

# 3. Генератор як нескінченний потік
# def infinite_counter():
#     i = 0
#     while True:
#         yield i
#         i += 1

# g = infinite_counter()

# print(next(g))  # 0
# print(next(g))  # 1

# ------------------------------------------------------

# 4. Coroutine-подібна поведінка (send)
# def accumulator():
#     total = 0
#     while True:
#         x = yield total 
# #Тут назовні із yield відправляється total,
#  а назад приходить значення для х
#         if x is not None:
#             total += x

# gen = accumulator()
# next(gen)  # запуск

# print(gen.send(10))  # 10
# print(gen.send(5))   # 15

# 👉 Генератор може приймати дані, не тільки віддавати
# В цьому прикладі генератор створюється, запускається методом некст 
# (Важливо запустити генератор для подвльшої його роботи),
# який повертає 0 як первоначальне значення і очікує вводу з методу сенд
#  і далі все повторюється у циклі
# Важливо розуміти, що send() працює лише після першого yield, тобто після виклику next()
# -----------------------------------------------------

# 5. Lazy кешування / memoization
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# f = fib()
# for _ in range(5): # naming _ shows that variable _ is never used
#     print(next(f))  # 0 1 1 2 3
# ------------------------------------------------------

# 6. Контроль виконання (state machine)
# def traffic_light():
#     while True:
#         yield "RED"
#         yield "GREEN"
#         yield "YELLOW"

# light = traffic_light()

# print(next(light))  # RED
# print(next(light))  # GREEN

# ----------------------------------------------------
# 7. Throttling / batching
# def batch(iterable, size):
#     it = iter(iterable)
#     while chunk := list(islice(it, size)):
#         yield chunk

# ----------------------------------------------------
# Коли використовувати генератори:
# великі дані
# стрімінг
# pipeline обробка
# нескінченні послідовності
# хочеш чистий код без класів
# 
# Коли НЕ треба
# потрібно багаторазове проходження
# потрібен random access (arr[5])
# логіка дуже проста → list ок

# Головна відмінність іткраторів від генераторів: ітератори це об'єкти, що повинні мати два
# обов'язкові методи __iter__() і __next__(), а генератори це методи в яких ітерування проводиться 
# за допомогою оператора yield та метода next(). При цьому для збереження стану ітератор використовує окрему змінну
# а генератор просто "заморожує" поточне значення повертаємої змінної.
# За рахунок "заморозки" генератори дозволяють економити пам'ять.
# Після завершення генератор "вмирає" і портібно створюівати новий, а ітератор можна використовувати багаторазовово.
# Генератори підтримують ввод даних завдяки send(), в той час як ітератори зазвичай цього не дозволяють

#  Homework
# Days of week generator

def get_week_day(): 
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    index = 0
    while True:
        yield week[index]
        index=(index+1)%7
        
g=get_week_day()
print(next(g))       
print(next(g))       
print(next(g))       
print(next(g))       
print(next(g))       
print(next(g))       
print(next(g))       
print(next(g))       
print(next(g))   

def even_odd():
    isOdd = True
    while True:  
        yield ('odd' if isOdd else 'even')
        isOdd = not isOdd

def even_odd2():
    while True:
        yield "odd"
        yield "even"        

gen = even_odd2()
print(next(gen))        
print(next(gen))        
print(next(gen))        
print(next(gen))        
print(next(gen))        


def infinite_squares():
    i = 1
    while True:
        yield i*i
        i+=1

gen2 = infinite_squares()
for i in range(100):
    print(next(gen2))
      


# -----   Generator expressions  -----------------------
# Generator expression — це короткий запис для створення генератора, майже як list comprehension, 
# але замість [] використовуються ().

squares = (x * x for x in range(5))

lst = [x * x for x in range(5)] #Generates whole list at once
gen = (x * x for x in range(100_000_000)) #Creates generator and will return one result at once on call next()
# gen wil not save in memory 100 mlns squares

# has_even = any(x % 2 == 0 for x in numbers)
# all_positive = all(x > 0 for x in numbers)
# longest = max(len(word) for word in words)

# -----------------------------------------------------
# Коли generator expression краще за list comprehension
# Використовуй generator expression, якщо:
# даних багато
# потрібно пройтись лише один раз
# результат одразу йде в sum, max, min, any, all
# не потрібен доступ по індексу

# -----------------------------------------------------
# Коли краще list comprehension
# Використовуй список, якщо:
# потрібен повторний прохід
# потрібен доступ через [index]
# потрібно одразу бачити всі значення
# даних небагато

