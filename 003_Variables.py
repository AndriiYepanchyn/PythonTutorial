# змінні — це імена, що посилаються на об’єкти
# немає strict encapsulation як у Java
# імпорт = виконання файлу
# глобальні змінні — майже завжди погана ідея

# Python:
# простий синтаксис, але не примітивна модель
# все — об’єкти
# змінні — це посилання, а не контейнери
# область видимості чітка (LEGB), але доступ — гнучкий


# Тип змінної визначається під час виконання:
# x = 10      # int
# x = "text"  # тепер str

# НЕ потрібно:
# int x = 10  

# Але можна підказувати типи (type hints):
# x: int = 10

# Python працює через посилання на об’єкти:

# a = [1, 2]
# b = a

# b.append(3)
# print(a)  # [1, 2, 3]

# a і b вказують на один об’єкт використовуючи посилання на нього

# Змінні є Immutable (створюється новий об’єкт) та Mutable:
# Immutable: int, float, str, tuple
# x = 5
# x += 1  # новий об'єкт

# Mutable: list, dict, set
# lst = [1, 2]
# lst.append(3)  # змінюється існуючий


# Область видимості розширюється відповідно до LEGB правила (див 020):
# Local - видимість в рамках блока кода
# Enclosing (вкладені функції)
# Global (модуль)
# Built-in - системні змінні видимі звідусіль


# global і nonlocal
# global
x = 10

def f():
    global x
    x = 20
# nonlocal (для вкладених функцій)
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20


#  Видимість між модулями (файлами)
# Структура:

# mypackage/
#     __init__.py
#     module1.py

# Імпорт:
# from mypackage import module1

# Імпорт
# import mymodule
# mymodule.x
# або
# from mymodule import x       

# private змінних немає відповідно до конвенції, замість цього є умовне приховування
# name manling
# _x= 10 #protected (by convence)
# __x = 15 # like private (name manling)

# Доступ до змінних 
# з іншого пакету
# import config
# print(config.VALUE)

# Через клас:
# class A:
#     x = 10

# print(A.x)

# ===== Часті помилки
# Зміна mutable за замовчуванням
# def func(lst=[]):  # погано
#     lst.append(1)

# Правильно:

# def func(lst=None):
#     if lst is None:
#         lst = []

# Плутанина з копіями
# a = [1, 2]
# b = a[:]  # копія

# type(x)
# isinstance(x, int)
