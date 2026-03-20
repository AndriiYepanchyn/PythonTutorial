import pickle

# pickle — це стандартний модуль у Python, який використовується для серіалізації та десеріалізації об’єктів.
# 🔹 Серіалізація (pickling) — перетворення Python-об’єкта (списку, словника, користувацького класу тощо) у байтовий потік.
# 🔹 Десеріалізація (unpickling) — відновлення об’єкта з байтового потоку назад у Python.
# Коли використовувати pickle
# Збереження стану об’єктів у файл для подальшого використання.
# Передача складних об’єктів між процесами (наприклад, у multiprocessing).
# Тимчасове кешування даних.
# ⚠️ Але небезпечно використовувати pickle для даних із ненадійних джерел — при unpickle можна виконати довільний код (це вразливість до RCE).

# Ключові функції
# pickle.dump(obj, file) — серіалізує у файл.
# pickle.load(file) — десеріалізує з файлу.
# pickle.dumps(obj) — серіалізує у байти.
# pickle.loads(bytes) — десеріалізує з байтів.


# У pickle протокол визначає формат серіалізації, 
# тобто те, як саме об’єкт буде перетворений у байтовий потік.
# Рівні протоколів
# protocol=0 — текстовий (ASCII).
# protocol=1 — старий двійковий.
# protocol=2 — з’явився в Python 2.3.
# protocol=3 — для Python 3.
# protocol=4 — Python 3.4 (підтримка дуже великих об’єктів).
# protocol=5 — Python 3.8 (оптимізація для великих даних, memoryview).
# Зазвичай варто вказувати protocol=pickle.HIGHEST_PROTOCOL.

# Навіщо потрібні протоколи
# Сумісність між версіями Python
# Старіші протоколи (0, 1, 2) гарантують, що дані можна відкрити навіть у старих версіях Python.
# Новіші (4, 5) — ефективніші, але не завжди сумісні зі старими інтерпретаторами.
# Оптимізація розміру та швидкості
# Протокол 0 (ASCII) читається як текст, але займає багато місця.
# Протокол 5 — компактний і швидкий, краще працює з великими об’єктами та memoryview.
# Підтримка нових можливостей
# Кожен новий протокол додає можливість серіалізувати складніші структури або робити це ефективніше. Наприклад:
# protocol=4 дозволив працювати з дуже великими об’єктами (>4GB).
# protocol=5 ввів out-of-band data — можна передавати великі масиви без копіювання, що критично для numpy/pandas.

# | Функція / Константа                      | Опис                                              | Приклад                                                                                                                                                                                               |
# | ---------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
# | **`pickle.dump(obj, file, protocol=…)`** | Серіалізує об’єкт у файл                          | `python\nimport pickle\nwith open("data.pkl", "wb") as f:\n    pickle.dump([1, 2, 3], f, protocol=pickle.HIGHEST_PROTOCOL)\n`                                                                         |
# | **`pickle.load(file)`**                  | Десеріалізує об’єкт із файлу                      | `python\nwith open("data.pkl", "rb") as f:\n    data = pickle.load(f)\nprint(data)\n`                                                                                                                 |
# | **`pickle.dumps(obj, protocol=…)`**      | Серіалізує об’єкт у **байти** (рядок)             | `python\nb = pickle.dumps({\"a\": 1})\nprint(b)\n`                                                                                                                                                    |
# | **`pickle.loads(bytes)`**                | Десеріалізує з байтового рядка                    | `python\nobj = pickle.loads(b)\nprint(obj)\n`                                                                                                                                                         |
# | **`pickle.HIGHEST_PROTOCOL`**            | Найновіший доступний протокол                     | `python\nprint(pickle.HIGHEST_PROTOCOL)  # напр. 5\n`                                                                                                                                                 |
# | **`pickle.DEFAULT_PROTOCOL`**            | Протокол за замовчуванням у Python                | `python\nprint(pickle.DEFAULT_PROTOCOL)\n`                                                                                                                                                            |
# | **`pickle.Pickler(file, protocol=…)`**   | Клас для налаштованої серіалізації                | `python\nwith open(\"obj.pkl\", \"wb\") as f:\n    p = pickle.Pickler(f, protocol=pickle.HIGHEST_PROTOCOL)\n    p.dump({\"x\": 42})\n`                                                                |
# | **`pickle.Unpickler(file)`**             | Клас для налаштованої десеріалізації              | `python\nwith open(\"obj.pkl\", \"rb\") as f:\n    u = pickle.Unpickler(f)\n    print(u.load())\n`                                                                                                    |
# | **`pickle.PicklingError`**               | Виняток при неможливості серіалізації             | `python\ntry:\n    pickle.dumps(lambda x: x+1)\nexcept pickle.PicklingError as e:\n    print(\"Помилка:\", e)\n`                                                                                      |
# | **`pickle.UnpicklingError`**             | Виняток при зламаних або небезпечних pickle-даних | `python\ntry:\n    pickle.loads(b\"not a pickle\")\nexcept pickle.UnpicklingError as e:\n    print(\"Помилка:\", e)\n`                                                                                |
# | **`pickle.whichmodule(obj, name)`**      | Дізнатися, з якого модуля походить об’єкт         | `python\nimport math\nprint(pickle.whichmodule(math.sin, \"sin\"))  # math\n`                                                                                                                         |
# | **`buffer_callback` (протокол 5)**       | Передача великих масивів «поза» основним потоком  | `python\nimport pickle, array\narr = array.array(\"i\", range(100))\n\nbuffers = []\nserialized = pickle.dumps(arr, protocol=5, buffer_callback=buffers.append)\nprint(\"Буферів:\", len(buffers))\n` |








honda = ('civic', 'grey', '2009', 
         ((1, 'James'),
          (2, 'Janette'),
          (3, 'Max')))

mazda = ('rx7', 'red', '2019', 
         ((1, 'James'),
          (2, 'Janette'),
          (3, 'Max')))

filename = 'C:\\PythonProjects\\HelloWorld\\write_pikle__binary_text.txt'
write_mode = 'wb'
with open(filename, write_mode) as write_file:
    pickle.dump(honda, write_file) # each object dumps separately
    pickle.dump(mazda, write_file)
    

read_mode = 'rb'
with open(filename, read_mode) as read_file:
   new_honda =  pickle.load(read_file) # returns tuple as it is 
   new_mazda =  pickle.load(read_file) # sequence is matter
   
   print(new_mazda) 
   print(new_mazda[0])
   model, color, year, owner = new_mazda
   
   print('model = ', model)
   
#    ---------------------------
# Серіалізація у пам’яті (рядок байтів)


numbers = [1, 2, 3, 4]

# У байти
pickled = pickle.dumps(numbers)
print(pickled)

# Назад у список
unpickled = pickle.loads(pickled)
print(unpickled)

data = {"a": [1, 2, 3], "b": "hello"}

# Старий протокол (0) – читабельний
print(pickle.dumps(data, protocol=0))

# Новий протокол (5) – компактний
print(pickle.dumps(data, protocol=5))


