import requests
# Бібліотека requests
# Для перевірки чи дозволяє сайт скрапити себе легально треба ввести в адресну строку після домену /robots.txt


# Це найпопулярніша Python-бібліотека для роботи з HTTP-запитами.
# Вона дозволяє відправляти GET, POST, PUT, DELETE та інші запити до веб-сервера, отримувати HTML-сторінки, API-відповіді у JSON, завантажувати файли.
# Основна перевага — простота використання порівняно з вбудованим urllib

# | Метод / Функція            | Опис                                             | Приклад                                              |
# | -------------------------- | ------------------------------------------------ | ---------------------------------------------------- |
# | `requests.get(url)`        | Виконати GET-запит                               | `r = requests.get("https://example.com")`            |
# | `requests.post(url, data)` | Виконати POST із даними                          | `r = requests.post(url, data={"k":"v"})`             |
# | `r.text`                   | Отримати відповідь як текст                      | `print(r.text)`                                      |
# | `r.content`                | Отримати "сирі" байти (наприклад, для зображень) | `open("img.png","wb").write(r.content)`              |
# | `r.json()`                 | Розпарсити JSON-відповідь у dict,                |                                                      |
# |                            | list (якщо json is array)                        | `data = r.json()`                                    |
# | `r.status_code`            | Код відповіді (200, 404, 500)                    | `if r.status_code==200:`                             |
# | `headers`                  | Передати заголовки                               | `requests.get(url, headers={"User-Agent":"..."})`    |
# | `params`                   | GET-параметри                                    | `requests.get(url, params={"q":"python"})`           |
# | `timeout`                  | Таймаут запиту                                   | `requests.get(url, timeout=5)`                       |
# | `cookies`                  | Робота з cookies                                 | `r.cookies` / `requests.get(url, cookies={"k":"v"})` |

# Параметри в requests передаються двома способами:
# Через формування повного URL рядка та через параметер params в методі get()
# Нижче дві еквивалентні строки:

# Формування повного рядку це створення строки яка повністю містить і URL запиту і параметри запиту у форматі:
# www.example.com/function_name?param1=arg1&param2=arg2&param3=arg3  
response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/count?starttime=2014-01-01&endtime=2014-01-02')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/count?'
params = {'starttime': '2014-01-01', 
            'endtime': '2014-01-02'}

response2 = requests.get(url, params = params)

print(response.status_code)

# розпарсити отриману відповідь можна:
# 1) Якщо структура відома - через датакласи
from dataclasses import dataclass
data = requests.get(url, params = params)

@dataclass
class User:
    id: int
    name: str
user = User(**data)

#Або безпечніше 
user = User(
    id=data.get("id"),
    name=data.get("name")
)

#  2) Якщо структура невідома працюємо як з dict
name = data["name"]
age = data.get("age", 0) #тут 0 значення за замовченням
# або
city = data["address"]["city"]
users = [User(**u) for u in data]
# User(**u) еквивалентно User(name = u['name'], age = u['age']) це зручна форма, коли ключи словника точно співпадають із полями об'єкту
# краще, не впади за відсутності поля
city = data.get("address", {}).get("city")

# Як обійти будь-який JSON: 
# Будь-який JSON = дерево:
# Object → Map
# Array → List
# Value → leaf

# потрібен рекурсивний обхід

result = []
def walk_json(data, path=""):
    if isinstance(data, dict):
        for key, value in data.items():
            walk_json(value, f"{path}.{key}" if path else key)

    elif isinstance(data, list):
        for i, item in enumerate(data):
            walk_json(item, f"{path}[{i}]")

    else:
        result.append(path, data) # або {"path": path, "value": data}
        

walk_json(data)  
print(result)  

# Якщо ти підеш далі з цим підходом, упрешся в:
# null / None значення
# різні типи в одному полі
# масиви з різною структурою
# дуже глибоку вкладеність (рекурсія може впасти)
# Якщо таким чином створити лише дерево лист з ключів, то для отримання 
# значень по ним ключи треба буде парсити більш детально ніж просто спліт по крапці, 
# а й враховувати що серед вкладений елементів є масиви
