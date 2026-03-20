import shelve
# shelve — просте key-value сховище на диску (як dict, але збережений у файлах).
# Ключі: тільки str
# Значення: будь-які pickle-сумісні об’єкти
# Під капотом: pickle + dbm
# Одного разу записане значення залишається в файлі доки не буде видалене, це може стати джерелом помилок при записі, зчитуванні даних
# Main operations    
# db["a"] = 123        # запис
# x = db["a"]          # читання
# del db["a"]          # видалення
# "a" in db            # перевірка

# Зміни в об'єктах не зберігаються автоматично, їх треба перезаписувати
# db["lst"] = []
# db["lst"].append(1)   # ❌ не збережеться

# Корректно
# lst = db["lst"]
# lst.append(1)  #This will apdate object in the heap but not on the db file
# db["lst"] = lst
# АБО
# shelve.open("data.db", writeback=True)


# All operation executes through the 'with' operator, and variable db is available inside it
# To write value into file use
with shelve.open("data.db") as db:
# With may be replaced as: db = shelve.open('data.db)  
    db["key1"] = "value 1"
    db["key2"] = "value 2"
    db["key3"] = "value 3"
    db["key4"] = "value 4"
    db["key5"] = "value 5"
    print('db = ', db)
    
    db["key5"] = 'New value 5'
    del db["key2"]
#If With replaced object should be closed: db.close()   
    
# Iteration
    print('Keys =', list(db.keys()))
    print('Values =', list(db.values()))
    print('Items =', list(db.items()))
 
#To get value use  
with shelve.open("data.db") as db:
    print('key 1 = ', db["key1"])
    # print('key 2 = ', db["key2"]) #Value removed before such call will return error
    print(db.get("key2")) #Return empty object
    print('key 3 = ', db["key3"])
    print('key 4 = ', db["key4"])
    print('key 5 = ', db["key5"])
    
# Параметри open
# shelve.open(
#     filename,
#     flag="c",   # 'r' read, 'w' write, 'c' create, 'n' new
#     writeback=False 
# # writeback = true garantee what changed value will be replaced in db immediatelly
#  # Please consider this if you updating a lot of data inside the with block

# )    
# Може створювати наступні типи файліів:
# data.db
# data.db.dat
# data.db.dir
# data.db.bak 
# Видаляти треба усі разом   

# Коли використовувати

# ✔ кеш
# ✔ прототипи
# ✔ невеликі локальні дані

# ❌ багатопотоковість
# ❌ велика БД
# ❌ міжмовна сумісність
    
# Альтернативи:
# pickle — один файл
# json — читабельно
# sqlite3 — надійніше
# redis — швидко, але сервер

    # while True:
    #     key = input('Input key: ')
    #     if('quit'==key):
    #         print('Exit input sequence')
    #         break
    #     value = db.get(key, "Value not found") 
    #     #'Value not found" is not mandatory param and may be skipped, this value returns if key is missing
    #     # This may be replaced with if key in db: 
    #     print('value = ', value)
    
     #Reverse sort of Keys
    keys = list(db.keys()) 
    print('Ordered keys: ', keys)
    keys.sort()
    print('Ordered keys: ', keys)
    keys.sort(reverse = False)
    print('Ordered keys: ', keys)
    keys.sort(reverse = True)
    print('Ordered keys: ', keys)
    
    # How to convert dictionary into shelve object directly
    
    university = shelve.open('university_file')
    university['schedules'] = {
            'monday': ['math', 'English', 'Java lessons', 'Python lessons'],
            'tuesday': ['swimming', 'Arts', 'Java lessons', 'Go lang lessons'],
            'wenesday': ['math', 'English', 'Java lessons', 'Python lessons'],
            'thursday': ['Chemistry', 'Phisics', 'Java lessons', 'Python lessons'],
            'friday': ['Java lessons', 'English', 'Oil developing', 'Chemistry']
        }
    
    university['tutors'] = {
            'Math': 'Leibnits',
            'Phisics': 'Nils Bor',
            'Chemistry': 'Lomonosov'
        }
    
    print(university['schedules']['friday'])
    university.close()