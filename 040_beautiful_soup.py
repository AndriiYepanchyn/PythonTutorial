# BEAUTIFUL SOUP - allows parse html pages

# | Метод / Функція                      | Опис                           | Приклад                                      |
# | ------------------------------------ | ------------------------------ | -------------------------------------------- |
# | `BeautifulSoup(html, "html.parser")` | Створення об’єкта з HTML       | `soup = BeautifulSoup(r.text,"html.parser")` |
# | `soup.title`                         | Повертає `<title>`             | `print(soup.title.text)`                     |
# | `soup.find(tag, attrs)`              | Знаходить перший елемент       | `soup.find("h1", {"class":"main"})`          |
# | `soup.find_all(tag)`                 | Знаходить усі елементи         | `soup.find_all("a")`                         |
# | `.text`                              | Витягує тільки текст без тегів | `link.text`                                  |
# | `.name`                              | Витягуе ім'я тегу              | 'li_tag.name() верне li
# | `.get("attr")`                       | Витягує значення атрибута      | `link.get("href")`                           |
# | `soup.select("css_selector")`        | Пошук за CSS-селекторами       | `soup.select("div.content > a")`             |
# | `soup.get_text()`                    | Витягує увесь текст сторінки   | `print(soup.get_text())`                     |
# | `.parent / .children`                | Навігація по DOM               | `tag.parent`, `list(tag.children)`           |
# | `.decompose()`                       | Видалити тег із DOM            | `tag.decompose()`                            |
# | `.content`							 | Повертає вмість складного тегу |												 |
# |										 | body, div etc				  |												 |
# | `.next_sibling`						 | Повертає наступний (prev)      |								     			 |
# |	`.previous_sibling`					 | тег того ж рангу				  |												 |
# | `.find_next_sibling`				 |Повертає тег без урахування 	  |												 |
# |										 |порожніх строк				  |												 |
# | `.findChildren`						 | Повертає дітей цього тегу	  |												 |


from bs4 import BeautifulSoup
import requests

html_string = """
	<!DOCTYPE html>
	<html>
	<head>
		<title>Web Development Page</title>
		<style type="text/css">
			
			h1{
				color: white;
				background: red;
			}

			li{
				color: red;
			}

			#css-li{
				color: blue;
			}

			.green{
				color: green;
			}

		</style>
	</head>
	<body>
		<h1>Web Development</h1>
		<h1 class="green">Web</h1>
		<h3>Programming Languages</h3>

		<ol>
			<li>HTML</li>
			<li id="css-li">CSS</li>
			<li class="green">JavaScript</li>
			<li class="green" id="python-li">Python</li>
		</ol>

	</body>
	</html>



"""

parsed_html = BeautifulSoup(html_string, 'html.parser') #May be also be XML parser

# print(parsed_html.body) #Отримуємо баді 
# print(parsed_html.body.h3) # отримуємо заданий хідер
# print(parsed_html.body.ol.li) # отримаємо ліст ітем, як елемент ордеред листа
# print(parsed_html.find('li')) # Шукає перший знайдений
# print(type(parsed_html.find('li'))) #Тип елементу тег
# print(parsed_html.find_all('li')) # Знаходить всі входення, повертає резалтсет як лист з них
# print(type(parsed_html.find_all('li')))
# print(parsed_html.find(id="css-li"))
# print(parsed_html.select('#css-li')[0]) #виконує пошук за css селекторами і повертає весь  тег цілком, # означає пошук по ід
# print(parsed_html.find_all(class_="green")) #пошук за класом, поверає резултсет як лист. _ is mandatory for reserved word class
# print(parsed_html.select(".green")[1]) # . це пошук по клас
# print(parsed_html.select("body"))

# | Селектор       | Що шукає         | Приклад                 |
# | -------------- | ---------------- | ----------------------- |
# | `tag`          | тег              | `select('li')`          |
# | `.class`       | class            | `select('.menu')`       |
# | `#id`          | id               | `select('#main')`       |
# | `A B`          | B всередині A    | `select('ul li')`       |
# | `A > B`        | прямий дочірній  | `select('ul > li')`     |
# | `[attr]`       | атрибут існує    | `select('[href]')`      |
# | `[attr=value]` | атрибут дорівнює | `select('[type=text]')` |



# html_elem = parsed_html.select("li")[0]
# print(html_elem.get_text()) #Повертає теxt що знаходиться між <tag> text </tag>
# print('-'*60)

# html_elem_list = parsed_html.select("li")

# for html_elem in html_elem_list:
# 	print(html_elem.get_text())

# green_class_elem_list = parsed_html.select("li")

# for html_elem in green_class_elem_list:
# 	print(html_elem.get_text())

# for html_elem in green_class_elem_list:
# 	print(html_elem.attrs)

# html_elem_list = parsed_html.select("li")[3]
# print(html_elem_list.attrs['id'])
# print(html_elem_list['class']) #Звертається до атрибуту з назвою "клас" та Витягує назву класу з тегу
# print(type(html_elem_list))


# data = parsed_html.body.contents
# print(data)
# print(data[7]) #data[1] equal parsed_html.body.contents[1]
# print("-"*80)
# print(parsed_html.body.contents)
# # print(parsed_html.body.contents[7].contents[1])
# print("-"*80)
# print(parsed_html.body.contents[4].next_sibling)
# print("-"*80)
# print(parsed_html.body.contents[7].contents[0].next_sibling.next_sibling.next_sibling)
# print("-"*80)
# data = parsed_html.find(id = "css-li").parent.parent #1st parent return ol, 2nd body
# print(data)
# print("-"*80)
# data = parsed_html.find(id = "css-li").find_next_sibling(id="python-li")
# print(data)
print("-"*80)
# data = parsed_html.body.findChildren()[2] #Deprecated replaced by find_all()
# data = parsed_html.body.find_all()[2] 
# print(data)

# =========================================================================
response = requests.get('http://quotes.toscrape.com/')
data = BeautifulSoup(response.text, 'html.parser')
quotes = data.find_all(itemprop = "text")
print("quotes size = ", len(quotes))
for i in quotes:
	print(i.getText(), '\n')