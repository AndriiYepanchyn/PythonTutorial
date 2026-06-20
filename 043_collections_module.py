# Модуль collections містить спеціалізовані контейнерні типи 
# даних, які розширюють можливості стандартних list, dict, set, 
# tuple.

# Швидка таблиця вибору
# | Тип         | Для чого                              |
# | ----------- | ------------------------------------- |
# | Counter     | Підрахунок елементів                  |
# | defaultdict | Автоматичні значення за замовчуванням |
# | OrderedDict | Контроль порядку ключів               |
# | deque       | Черга, стек, буфер                    |
# | namedtuple  | Іменовані кортежі                     |
# | ChainMap    | Об'єднання словників                  |
# | UserDict    | Власний словник                       |
# | UserList    | Власний список                        |
# | UserString  | Власний рядок                         |

# Найпопулярніші на практиці

# У реальних проєктах найчастіше використовуються:
# Counter
# defaultdict
# deque
# namedtuple
# ChainMap

# Саме ці п'ять типів зустрічаються регулярно при роботі з файлами, 
# SQL, обробці даних, алгоритмами та веб-розробці.




from collections import Counter

# =======  Counter - Лічильник елементів. Створює аналог словника виду:


# {
#     "apple": 3,
#     "banana": 2
# } Тобто рахує скільки раз елемент додано до каунтеру

# Коли використовувати
# підрахунок слів;
# статистика символів;
# аналіз текстів;
# побудова рейтингів.

c = Counter()
c = Counter("hello")  #Для строки буде рахувати кількість символів
# print(c)

# Щоб рахувати окремі слова треба стрінг поділити на окремі слова, наприклад, через split
string = "Hello my dear friend how are you you even don't know hoe I miss you"
# print(Counter(string.split())) # ,.!? are matter

# c.clear() # Reset the counter

# +c #Remove zero and negative counts

# Accordingly converts counter to the list, set, dict
# list(c)
# set(c)
# dict(c)

# print(c.items()) #Convert c to a list of (elem, cnt) pairs



c = Counter(["apple", "apple", "banana"]) #Для списку він опирається на окремі елементи
# print(c)

# Додавання елементів
c["apple"] +=1
# print(c)

# Updating counter
c.update(["apple", "banana"])
# print(c)

# Delete item
del c["banana"]  #Complete delete element
# print(c)

c.subtract(["apple"]) #Reduce element count
# print(c)

c.update(["apple", "banana", "pine apple", "pickles", "tomato", "cucumber"])
c.update([ "pine apple", "pickles"])

# print(c.most_common()) #Returns All
# print(c.most_common(3)) #Return three most common elements

# Загальна кількість елементів
# print(c)
# print(f"{type(c)} contains total {c.total()},  elements")


# Арифметичні дії з каунтером

c1 = Counter(['One', 'Two', 'Three', 'White', 'Blue', 'Blue'])
c2 = Counter(['Yellow', 'Blue', 'White', 'Green', 'White'])
# print( 'Addition ', (c1 + c2))
# print('Subtraction ', c1 - c2)

# min (intersection of two counters, from two equal elements stay that one which has min count)
# print('Min ', c1 & c2)  
# max (Concatenation of two counters, from equal elements stay that one which has max count)
# print('Max ', c1 | c2)  


# =====  defaultdict Словник зі значенням за замовчуванням.  =====


# Коли використовувати
# групування даних;
# підрахунок;
# індексація.

from collections import defaultdict

d = defaultdict(list) 
#Argument is default object which will be returned if the key is absent
d["group1"].append("John") #Add element
# print(d)

d = defaultdict(int)
d["a"] += 1
# print(d)

d = defaultdict(set)
d["group"].add("John")
d["group"].add("Catty")
d["group"].add("John")
# print(d)

d = defaultdict(float)
# print(d)
d = defaultdict(lambda: "Unknown") #Will return result of the lambda function
# print(d)


# =====  OrderedDict  Словник зі збереженням порядку вставки.  ======

# Коли використовувати
# LRU-кеші;
# контроль порядку елементів.

from collections import OrderedDict

d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 4
d["d"] = 3

# print(d)

# Перемістити ключ
d.move_to_end("c")
# print(d)

# Видалити перший/останній
d.popitem(last=True)
# print(d)

d.popitem(last=False)
# print(d)


# =====  deque (Double Ended Queue)  =====

# Черга з доступом до початку та кінця.
# Працює значно швидше за list для вставки/видалення на початку.
# Коли використовувати
# FIFO черги;
# LIFO стеки;
# буфери;
# історія команд;
# sliding window алгоритми.


from collections import deque

# Створення
d = deque()
d = deque([1, 2, 3])

# Додавання в кінець
d.append(4)

# Додавання в початок
d.appendleft(0)

# Видалення з кінця
d.pop()

# Видалення з початку
d.popleft()

# Обмеження розміру, при додаванні старі елементи будуть видалятись
d = deque([1, 2, 3, 4, 5, 6, 7, 8], maxlen=5)
# d = deque([1, 2, 3, 4, 5, 6, 7, 8])
# print("initial deque ", d)
# print("deque with maxlen = 5 ", d)
d.appendleft(0)
# print("deque appendleft 0 ", d)
d.append(9)
# print("deque append 9", d)

# Обертання на N елементів вліво чи вправо

d.rotate(1)
# print("deque rotate(1)", d)
d.rotate(-3)
# print("deque rotate(-3)", d)



#  =====  namedtuple  Кортеж з іменованими полями.  ======


# immuttable object
# Коли використовувати
# DTO;
# результати SQL-запитів;
# легкі моделі даних.

from collections import namedtuple

# Підготовка класу об'єкту
Person = namedtuple(
    "Person",
    ["name", "age"]
)

# Створення об'єкту
p = Person("John", 25)

# Another way
Person2 = namedtuple("Person2", "name age")
p2 = Person2(name = 'Bob', age = 30)
p3 = Person(name = 'ZiziTop', age =85)


print('Name: ', p.name, 'Age: ', p.age)
print('Name 2: ', p2.name, 'Age: ', p2.age)
print('Name 3: ', p3.name, 'Age: ', p3.age)

# Перетворення в словник
# print('Initial ', type(p), '; ', p)
# print('Asdict ', type(p._asdict()), '; ', p._asdict() )

# Перетворити в tuple
# print('As tuple: ', type(tuple(p)), ': ', p)

# Заміна значення
p2 = p._replace(age = 30)  #Remember tuple is immutable
# print('Replaced ', p2)


# =====  ChainMap   =====


# Об'єднує кілька словників без копіювання.
# Коли використовувати
# налаштування програми;
# об'єднання конфігурацій;
# об'єднання словників без копіювання.

from collections import ChainMap

d1 = {"a": 1}
d2 = {"b": 2}

cm = ChainMap(d1, d2)

# print(cm)
# print(cm['b'])

# Додавання
# Нові значення потрапляють у перший словник.
cm["c"] = 3

# print(cm)

# =====  UserDict  =====

# Базовий клас для створення власного словника.
# Коли використовувати
# Коли потрібно перевизначати поведінку словника.

from collections import UserDict

class MyDict(UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(
            key.upper(),
            value
        )


# =====  UserList  =====

# Базовий клас для власного списку.  
# Коли використовувати
# Коли потрібно розширити list.      

from collections import UserList

class PositiveList(UserList):

    def append(self, item):
        if item > 0:
            super().append(item)



# =====  UserString  =====
# Базовий клас для власного рядка.

from collections import UserString

class UpperString(UserString):

    def __init__(self, value):
        super().__init__(value.upper())