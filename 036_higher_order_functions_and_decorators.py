# ------  1. Higher Order Functions ---------

# Higher Order Function — це функція, яка:
# приймає іншу функцію як аргумент
# або повертає функцію

# Щоб зрозуміти що в якості аргумента очікується функція можна використовувати type hints через Callable

from typing import Callable
# def apply(func: Callable, value: int) -> int:
#     return func(value)
# Але краще вказувати ще аргументи та тип повернення:
# def apply(func: Callable[[int], int], value: int) -> int:
#     return func(value)
# Тут:

# Callable[[int], int]
# перший int — тип аргументу функції
# другий int — тип, який вона повертає

# Тобто func має бути приблизно такою функцією:
# def square(x: int) -> int:
#     return x * x
# Для sorted() аналог міг би виглядати так:
# Тут видно, що key повинна бути функцією, яка:
# приймає str
# повертає будь-яке значення для сортування
# from typing import Callable, Any
# def my_sorted(
#     items: list[str],
#     key: Callable[[str], Any]
# ) -> list[str]:
#     return sorted(items, key=key)

# def set_handler(handler: Callable[[], None]) -> None:
#     handler()
# Це означає:

# функція без аргументів
# нічого не повертає

# Тобто Callable — головний спосіб явно показати, що параметр повинен бути функцією.   
# -------------------------------------------------------

# def greet(name):
#     return f"Hello, {name}!"


# def run_function(func, value):
#     return func(value)


# result = run_function(greet, "Andrew")
# print(result)

# Функцію можна зберігати у змінній
# Дужки () означають виклик функції. Без дужок ти передаєш сам об'єкт функції.
# from random import choice
# def say_hello():
#     cases = ['Hello', 'Bonjour', 'Aloha', 'Conitua', 'Вітаю']
#     print(choice(cases))

# my_func = say_hello

# my_func()      # Hello
# say_hello()    # Hello
# print(say_hello)     # <function say_hello at ...>
# print(say_hello())   # Hello

# Передача функції як аргументу
# def square(x):
#     return x * x

# def cube(x):
#     return x * x * x

# def apply(func, value):
#     return func(value)

# print(apply(square, 4))  # 16
# print(apply(cube, 4))   

# 4. Повернення функції з іншої функції
# def make_multiplier(n):
#     def multiplier(x):
#         return x * n

#     return multiplier


# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(10))   # 20
# print(triple(10))   # 30

# -----  5. Замикання (Closure)  -------
# Closure — це функція, яка "пам'ятає" змінні з зовнішньої області видимості.
# nonlocal: 
# змінна має вже існувати у зовнішній функції
# nonlocal дозволяє читати і змінювати її з внутрішньої функції
# після зміни нове значення буде видно і у внутрішній, і у зовнішній функції
# але створити нову зовнішню змінну через nonlocal не можна

# def counter():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment


# c = counter()

# print(c())  # 1
# print(c())  # 2
# print(c())  # 3

# -----  6. Вбудовані Higher Order Functions  ------
# map() - Застосовує функцію до кожного елемента.
# filter() - Залишає лише ті елементи, для яких функція повертає True.
# sorted() - Сортує елементи
# reduce() - reduce() знаходиться в модулі functools.

# numbers = [1, 2, 3, 4]
# result = map(lambda x: x * 2, numbers)
# print(list(result))
# # [2, 4, 6, 8]
# # -----------------------
# numbers = [1, 2, 3, 4, 5, 6]
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))
# [2, 4, 6]
# ------------------------
# words = ["banana", "kiwi", "apple", "watermelon"]
# result = sorted(words, key=len) # key= приймає будь-яку функцію, яка для кожного елемента повертає значення, по якому треба сортувати.
# sorted(words, key=len, reverse=True) # Можна ще комбінувати з reverse=True:
# print(result)
# ['kiwi', 'apple', 'banana', 'watermelon']

# sorted(words, key=len) #Тут len повертає довжину рядка.
# sorted(words, key=str.lower) #Сортування без врахування регістру:
# sorted(words, key=lambda word: word[-1]) #Сортування по останній букві:
# sorted(words, key=lambda word: sum(1 for ch in word.lower() if ch in "aeiou"))
# Сортування по кількості голосних

# Для списку словників:
# students = [
#     {"name": "John", "age": 20},
#     {"name": "Alice", "age": 18},
#     {"name": "Bob", "age": 22}
# ]
# sorted(students, key=lambda student: student["age"])
# sorted(students, key=lambda student: student["name"])

# Для кортежів:

# data = [
#     ("John", 85),
#     ("Alice", 92),
#     ("Bob", 78)
# ]

# sorted(data, key=lambda item: item[1]) # По другому елементу:
# sorted(data, key=lambda item: item[0]) # По першому елементу:

# Сортування по декількох полях одразу:
# students = [
#     {"name": "John", "age": 20},
#     {"name": "Alice", "age": 20},
#     {"name": "Bob", "age": 18}
# ]
# sorted(students, key=lambda student: (student["age"], student["name"])) # Спочатку по віку, потім по імені:

# -----  7. lambda-функції  ------
# square = lambda x: x * x
# print(square(5))

# add = lambda a, b: a + b
# print(add(2, 3))

# students = [
#     ("John", 85),
#     ("Alice", 92),
#     ("Bob", 78)
# ]
# sorted_students = sorted(students, key=lambda student: student[1])
# print(sorted_students)

# ------  8. Декоратори  -------------------------------
# Декоратор — це функція, яка змінює поведінку іншої функції.
# декоратор це функція вищого порядку в яку передається функція як аргумент. 
# І виклик декоратора виконується через @<decorator_name> перед функцією-аргументом
# Головне — після @ має стояти ім'я функції-декоратора або виклик функції, яка повертає декоратор.

# Декоратор — це спеціальний випадок higher order function:

# він приймає функцію як аргумент
# зазвичай повертає нову функцію
# нова функція обгортає стару та додає нову поведінку

# Навіщо потрібні декоратори

# Типові задачі:

# логування
# перевірка прав доступу
# вимірювання часу виконання
# кешування
# повторні спроби
# валідація аргументів


# Базовий синтаксіс:

# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")

# Важливо повертати wrapper це дає змогу зробити відкладений виклик,
#  без нього декротатор викликається відразу при створенні функції
#     return wrapper 


# @decorator #Якщо функція-декоратор має інше ім'я то використовуєсться те ім'я
# def say_hello():
#     print("Hello")

# say_hello()

# Це еквівалентно:
# def say_hello():
#     print("Hello")

# say_hello = decorator(say_hello)

# 9. Декоратор з аргументами
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before")

#         result = func(*args, **kwargs)

#         print("After")
#         return result

#     return wrapper


# @decorator
# def add(a, b):
#     return a + b


# print(add(2, 3))

# 11. Декоратор для вимірювання часу
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()

#         result = func(*args, **kwargs)

#         end = time.time()
#         print(f"Execution time: {end - start:.4f} sec")

#         return result

#     return wrapper

# @timer
# def slow_function():
#     time.sleep(1)

# slow_function()

# Декоратор з параметрами
# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hi():
#     print("Hi")

# say_hi()

# Кілька декораторів
# def decorator1(func):
#     def wrapper():
#         print("Decorator 1")
#         func()
#     return wrapper


# def decorator2(func):
#     def wrapper():
#         print("Decorator 2")
#         func()
#     return wrapper


# @decorator1
# @decorator2
# def hello():
#     print("Hello")

# hello()    

# ------  functools.wraps  --------
# functools.wraps потрібен, щоб після декорування зберегти метадані оригінальної функції:

# ім'я функції
# docstring
# модуль
# анотації
# посилання на оригінальну функцію

# Без wraps декорована функція фактично стає wrapper.
from functools import wraps


# def decorator(func):
#     @wraps(func) #This line allows us get real name of decorated function (greet in our example)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)

#     return wrapper

# @decorator
# def greet(name):
#     """Print greeting message"""
#     return f"Hello, {name}"

# print('----- Checking wraps: -----')
# print(greet.__name__)
# print(greet.__doc__)

# print(greet('Andrii'))


# Можна блокувати використання якогось типу аргументів завдяки декораторам
def prohibit_kwargs(func):
    def wrapper(*args, **kwargs):
        if kwargs:
              raise ValueError('Kwargs are prohibited')
        return func(*args)
    return wrapper

@prohibit_kwargs
def test_function(*args, **kwargs):
    print('test function has *args: ', args)
    print('test function has *kwargs: ', kwargs )


test_function('arg1', 'arg2', ['arg3', 'arg4'])
try:
     test_function('arg1', 'arg2', ['arg3', 'arg4'], key1 = 'key1', key2 = 'key2')
except ValueError as e:
    print('Test function caused Error: ', {e})




# Часті помилки:
# Помилка 1: виклик функції замість передачі
# apply(square(), 5) #Неправильно
# apply(square, 5) #Правильно

# Помилка 2: забути return у wrapper
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result

#     return wrapper

# Помилка 3: декоратор не підтримує аргументи
# wrapper майже завжди повинен використовувати *args, **kwargs
# def wrapper(*args, **kwargs):
#     return func(*args, **kwargs)


# ------  Homework  ---------------------------
# def print_args(func : Callable):
#         @wraps(func) 
#         def wrapper(*args, **kwargs):
#             print('decorator function has *args: ', args)
#             print('decorator function has *kwargs: ', kwargs )
#             return func(*args, **kwargs)

#         return wrapper

# @print_args
# def test_function(*args, **kwargs):
#     print('test function has *args: ', args)
#     print('test function has *kwargs: ', kwargs )


# test_function('arg1', 'arg2', ['arg3', 'arg4'], key1 = 'key1', key2 = 'key2')


# def hello_from_decorator(func : Callable):
#      def wrapper(*args, **kwargs):
#           return 'Hello from decorator, ' + func(*args, **kwargs)
#      return wrapper
     

# @hello_from_decorator
# def return_name(name):
#     return str(name) 

# print(return_name("Andrii"))

 
# # Заборона більше ніж два аргументи
# def prohibit_2args(func):
#     def wrapper(*args, **kwargs):
#         if len(args) + len(kwargs) >2:
#               raise ValueError('2+ arguments are prohibited')             
#         return func(*args, **kwargs)
#     return wrapper

# @prohibit_2args
# def test_function(*args, **kwargs):
#     print('test function has *args: ', args)
#     print('test function has *kwargs: ', kwargs )


# try:
#     test_function('arg1', 'arg2')
# except ValueError as e:
#     print('Test function caused Error: ', {e})
# try:
#     test_function('arg1', 'arg2', 'arg3', ['arg3', 'arg4'])
# except ValueError as e:
#     print('Test function caused Error: ', {e})
# try:
#     test_function('arg1',  key1 = 'key1')
# except ValueError as e:
#     print('Test function caused Error: ', {e})
# try:
#     test_function('arg1', 'arg2', ['arg3', 'arg4'], key1 = 'key1', key2 = 'key2')
# except ValueError as e:
#     print('Test function caused Error: ', {e})

import time
from functools import wraps

def wait(delay):
    def decorator(func : Callable):
        @wraps(func) 
        def wrapper(*args, **kwargs):
            time.sleep(delay)
            result = func(*args, **kwargs)
            print(f'There was a pause {delay} seconds before execution {func.__name__}')
            return result
        return wrapper
    return decorator


@wait(3)
def say_smth():
    print('I know your secret!!!')

print("What I gonna to say...")
say_smth()