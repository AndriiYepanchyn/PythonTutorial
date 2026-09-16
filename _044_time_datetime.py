# Модуль time використовується для:

# роботи з поточним часом;
# вимірювання тривалості виконання;
# затримок (sleep);
# перетворення часу між різними форматами.
# Час представлено двома видами: 
# timestamp - float означає кількість секунд  що пройшла з епохи Юнікс (1.1.1970)
# struct_time - namedtuple який включає опис років, місяців, днів, часу через пари ключ - значення

# struct_time Створюється через:
# time.localtime()
# time.gmtime()
# time.strptime()


# | Функція               | Для чого                |
# | --------------------- | ----------------------- |
# | `time.time()`         | Unix timestamp          |
# | `time.sleep()`        | Затримка                |
# | `time.localtime()`    | Локальний час           |
# | `time.gmtime()`       | UTC час у struct_time   |
# | `time.strftime()`     | Форматування            |
# | `time.strptime()`     | Парсинг                 |
# | `time.mktime()`       | struct_time → timestamp |
# | `time.perf_counter()` | Benchmark               |
# | `time.monotonic()`    | Таймаути                |
# | `time.process_time()` | Чистий CPU-час          |



import time

# =====  Отримання поточного часу  =====
# Повертає кількість секунд від епохи Unix (01.01.1970 UTC).
# Return timestamp of float in seconds
now = time.time()
print('Current time: ', now)  


#  =====  Остановка процесу  ======
#  Зупиняє виконання на зазначену кількість секунд
time.sleep(0.5) #pause execution for 0,5 seconds


# =====  LocalTime  =====
# Повертає локальний час з урахуванням часового поясу у
# вигляді структури struct_time.

# | Поле     | Опис                     |
# | -------- | ------------------------ |
# | tm_year  | Рік                      |
# | tm_mon   | Місяць (1-12)            |
# | tm_mday  | День місяця              |
# | tm_hour  | Година                   |
# | tm_min   | Хвилина                  |
# | tm_sec   | Секунда                  |
# | tm_wday  | День тижня (0=понеділок) |
# | tm_yday  | День року                |
# | tm_isdst | Літній час               |

t = time.localtime() 
print('Local time: ', t)
print('Local time fields: ', t.tm_mday, '.', t.tm_mon, '.', t.tm_year)


# =====  UTC та DST час  ======
# time.gmtime() - Повертає час у UTC. Лондонський час з моменту початку Юнікс епохи тобто 1.1.1970
# Також слід вважати на DST (Day saving Time) який також бере до уваги літній та зимовий час
# Результат також повертається у вигляді  struct_time.

utc = time.gmtime()
time1 = time.localtime()
print('UTC time: ', utc)
print('='*40)
print('Localtime: ', time1)


# =====  Форматування дати  time_tuple в строку =====
# time.strftime(format)
# Повертає дату у вигляді строки відповідно до заданого формату.

# | Формат | Значення     |
# | ------ | ------------ |
# | %Y     | Рік (2025)   |
# | %y     | Рік (25)     |
# | %m     | Місяць       |
# | %d     | День         |
# | %H     | Година 00-23 |
# | %I     | Година 01-12 |
# | %M     | Хвилини      |
# | %S     | Секунди      |
# | %A     | Назва дня    |
# | %B     | Назва місяця |
# | %p     | AM/PM        |

# print(time.strftime("%Y-%m-%d"))
now = time.strftime("%d.%m.%Y %H:%M:%S")
print('Type of strftime() now: ', now, ' ', type(now))

tup = (2025, 6, 21, 14, 30, 0, 5, 172, -1) #Це обов'язковий формат таплу
date = time.strftime("%d.%m.%Y %H:%M:%S", tup)
print('Type of strftime() date from tuple: ', date, ' ', type(date))

# Зробити корреткний формат таплу не зручно, тому частіше роблять наступним чином
t = time.strptime("2025-06-21", "%Y-%m-%d")
print(time.strftime("%d.%m.%Y", t))


# =====  Парсинг дати float в string  ======
# Дата рахується в флоат секундах з початку епохи
print("Current time: ", time.ctime(time.time()))


# =====  Парсинг рядка в дату формату struct_time =====
# time.strptime() - Розбирає рядок відповідно до шаблону.

s = "2025-06-21"
t = time.strptime(s, "%Y-%m-%d")
print('time.strptime: ',t, 'Type of t: ', type(t))

# ======  Конвертація struct_time → timestamp  =====
# time.mktime()
t = time.strptime(
    "2025-06-21",
    "%Y-%m-%d"
)

timestamp = time.mktime(t) # return timestamp from time_struct
# print(timestamp)

# =====  Convert time tuple to the string  ======
print(time.asctime()) 

# =====  Timestamp → string  ======
# Convert time to the formatted string accordingly to the specified format

ts = time.time()

print(
    time.strftime(
        "%Y-%m-%d %H:%M:%S",
        time.localtime(ts)
    )   
)

time.perf_counter()


# =====  Найточніший таймер для вимірювання продуктивності.  =====
#  suffix _ns in function name allow get result in nanoseconds but not in seconds

start = time.perf_counter()
for i in range(1000000):
    pass
end = time.perf_counter()
# print(end - start)

# ======  Монотонний час  ======
# time.monotonic()
# Гарантовано не зменшується.
# Підходить для таймаутів.

start = time.monotonic()
time.sleep(2)
elapsed = time.monotonic() - start
# print(elapsed)


# =====  Процесорний час  ======
# time.process_time()
# Враховує тільки час роботи CPU.
# Не враховує:
# sleep
# очікування I/O

start = time.process_time()
for i in range(10000000):
    pass
# print(
#     time.process_time() - start
# )



# ======  Timezone Constants  ======
# READ MANUAL BEFORE USE THIS CONSTANTS 


print('  UTC time', time.strftime('%Y.%m.%d %H:%M:%S', time.gmtime()))
print('local time', time.strftime('%Y.%m.%d %H:%M:%S', time.localtime()))

# Here we may see the difference in time between two timezones
# Return offset of the local DST timezone in seconds West of UTC if defined
print('time.altzone min = ', time.altzone/60) #Use only if daylight is Nonezero

# return nonsezo value if timezone is defined
print('time.daylight min = ', time.daylight/60)

# Return offset between local non-DST timezone and ow UTC
print('time.timezone min = ', time.timezone/60)

# return tuple of two names: local nonDST timezone and local DST timezone
print('time.tzname min = ', time.tzname) 


