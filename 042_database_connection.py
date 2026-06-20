from pathlib import Path
import sqlite3  

dbfile = Path(__file__).parent / "resources" / "sql-lite.db"

conn = sqlite3.connect(dbfile) # If file is not exist it will be created 
# conn = sqlite3.connect(":memory:") #Creates db in memory, erases after program is stopped
cursor = conn.cursor() #Cursor is the object responsible for interaction with db

query = """
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    age INTEGER,
    grade REAL
)
"""

cursor.execute(query) #Allow execute the query

# conn.commit() #Allow to save changes in db

# conn.close() #Close connection and disable the database interaction


# | Метод           | Призначення              | Повертає дані?  |
# | --------------- | ------------------------ | --------------  |
# | `execute()`     | один запит -             | ❌ ні           |
# |                 |use for not SELECT        |                 |
# | `executemany()` | багато однакових запитів | ❌ ні           |
# | `fetchone()`    | читання                  | ✅ так          |
# | `fetchall()`    | читання                  | ✅ так          |
# | 


# execute() execute query and return cursor which contains result
cursor.execute("""
INSERT INTO students(name, surname, age, grade)
VALUES ('John', 'Dow', 20, 4.5)
""")

# This allow to insert multiple parameters
# cursor.execute(
#     """
#     INSERT INTO students(name, age)
#     VALUES (?, ?)
#     """,
#     ("John", 20)
# )


# BATCH INSERT
students = [
    ("John", "Snow", 20),
    ("Mary", "Kury", 22),
    ("Tom", "Lee Jones", 18)
]

# executemany doesn't return any values
# What may be get from cursor after executemany:
#  - quantity of processed rows: cursor.rowcount
#  - last set id (limited ability):  cursor.lastrowid
#  - executemany() НЕ використовується для:
# SELECT отримання даних
# Він призначений тільки для: INSERT, UPDATE, DELETE

cursor.executemany(
    """
    INSERT INTO students(name, surname, age)
    VALUES (?, ?, ?)
    """,
    students
)

conn.commit()


# How to get data from cursor:
cursor.execute("""
INSERT INTO students(name, surname, age, grade)
VALUES ('John', 'Snow', 20, 4.1),
       ('Mary', 'Stuart', 23, 4.2),
       ('Tommy', 'Lee Johnes', 24, 4.5),
       ('Albert', 'Van Vogt', 25, 3.5)                       
""")

cursor.execute(
    "SELECT * FROM students"
)

print('===== fetchone  =====')
row = cursor.fetchone()
print('type = ', type(row), '; returned data = ', row)

print('===== fetchmany(2)  =====')
rows = cursor.fetchmany(2)
for row in rows:
    print(row)

print('===== fetchall  =====')
rows = cursor.fetchall()
for row in rows:
    print(row)


# IMPORTANT every next fetch doesn't include previous fetch result

# ======  Iteration through the result =====
cursor.execute(
    "SELECT * FROM students"
)

for row in cursor:
    print(row) #row is the tuple

# Column access

conn.row_factory = sqlite3.Row #This shoud be first step
cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM students"
)

row = cursor.fetchone()

print(row["name"])
print(row["age"])

# ======  Transactions  =======

# Manual management
# try:
#     conn.execute("BEGIN")

#     cursor.execute(...)
#     cursor.execute(...)

#     conn.commit()

# except Exception:
#     conn.rollback()
#     raise

# Autocommit/rollback

# The following will make rollback on error
with sqlite3.connect("students.db") as conn:
    conn.execute(
        """
        INSERT INTO students(name)
        VALUES(?)
        """,
        ("John",)
    )

# ===== Execution of SQL file  =======

# with open("schema.sql") as file:
#     sql = file.read()

# cursor.executescript(sql)

# ======  Check if table exist
# cursor.execute("""
# SELECT name
# FROM sqlite_master
# WHERE type='table'
# AND name='students'
# """)

# exists = cursor.fetchone() is not None

# ===== Get list of all tables

# cursor.execute("""
# SELECT name
# FROM sqlite_master
# WHERE type='table'
# """)

# print(cursor.fetchall())



# =======  SQL Injections  ======

# The following construction is unsafe user may enter name as
# ' OR 1=1 --
# And this allow to get all records
# name = input()

# cursor.execute(
#     f"SELECT * FROM students WHERE name='{name}'"
# )


# How to evoid sql injections? 
# use parametrised queries

# name = input()

# cursor.execute(
#     "SELECT * FROM students WHERE name=?",
#     (name,)
# )


# =====  Main errors ======
# sqlite3.Error
# sqlite3.DatabaseError
# sqlite3.OperationalError
# sqlite3.IntegrityError
# sqlite3.ProgrammingError

# Короткі правила

# ✅ Завжди використовуй ? для параметрів
# ✅ Викликай commit() після INSERT/UPDATE/DELETE
# ✅ Використовуй with sqlite3.connect(...)
# ✅ Вмикай PRAGMA foreign_keys = ON
# ✅ Для великих вибірок ітеруйся по cursor, а не fetchall()
# ✅ Використовуй індекси для колонок, які часто беруть участь у WHERE, JOIN, ORDER BY

# ❌ Не формуй SQL через f-string або конкатенацію рядків
# ❌ Не забувай rollback() у транзакціях
# ❌ Не зберігай паролі у відкритому вигляді в SQLite або будь-якій іншій БД.


# Чи потрібен окремий курсор для кожного запиту?
# Не обов'язково.
# Можна використовувати один:
# cursor.execute("SELECT * FROM students")
# ...

# cursor.execute("SELECT * FROM teachers")
# ...
# Але новий execute() перезапише попередній результат.

# Кілька курсорів одночасно
# Іноді корисно:
# c1 = conn.cursor()
# c2 = conn.cursor()

# c1.execute("SELECT * FROM students")
# c2.execute("SELECT * FROM teachers")
# Кожен курсор має власний стан і власну позицію в результатах.

# Чи можна обійтися без курсора?
# Методи Connection.execute() автоматично створюють внутрішній курсор:
# for row in conn.execute(
#     "SELECT * FROM students"
# ):
#     print(row)

# Найчастіше використовувані методи Cursor
# | Метод             | Призначення                 |
# | ----------------- | --------------------------- |
# | `execute()`       | виконати один SQL-запит     |
# | `executemany()`   | виконати запит багато разів |
# | `executescript()` | виконати SQL-скрипт         |
# | `fetchone()`      | отримати один рядок         |
# | `fetchmany(n)`    | отримати N рядків           |
# | `fetchall()`      | отримати всі рядки          |
# | `close()`         | закрити курсор              |
# | `lastrowid`       | ID останнього INSERT        |
# | `rowcount`        | кількість змінених рядків   |

# Another one common way to use sqlite
# with sqlite3.connect("students.db") as conn:
#     conn.row_factory = sqlite3.Row

#     rows = conn.execute(
#         """
#         SELECT *
#         FROM students
#         WHERE age > ?
#         """,
#         (18,)
#     )

#     for row in rows:
#         print(row["name"])