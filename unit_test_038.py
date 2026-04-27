
import unittest
from test_sourсe_038 import StringMethods as Source

# | Метод                | Коли викликається         | Обов'язковість | Параметри      | Нюанси                                 |
# | -------------------- | ------------------------- | -------------- | -------------- | -------------------------------------- |
# | `setUp(self)`        | Перед КОЖНИМ тестом       | ❌              | -              | Часто використовують для ініціалізації |
# | `tearDown(self)`     | Після КОЖНОГО тесту       | ❌              | -              | Очистка ресурсів                       |
# | `setUpClass(cls)`    | 1 раз перед усіма тестами | ❌              | `@classmethod` | Дорогі ініціалізації                   |
# | `tearDownClass(cls)` | 1 раз після всіх тестів   | ❌              | `@classmethod` | Закриття з’єднань і т.д.               |

# | Метод                     | Перевіряє          | Параметри         | Нюанси                       |
# | ------------------------- | ------------------ | ----------------- | ---------------------------- |
# | `assertEqual(a, b)`       | `a == b`           | `a, b`            | перевіряє рівність двох параметрів
# |                           |                    |                   |a = test_method, b= expected result
# | `assertAlmostEqual(a, b)` | Для float          | `places=7` (опц.) | Не порівнюй float через `==` |
# | `assertNotEqual(a, b)`    | `a != b`           | `a, b`            | Перевіряє нерівність                             |
# | `assertTrue(x)`           | `bool(x) is True`  | `x`               |                               |
# | `assertFalse(x)`          | `bool(x) is False` | `x`               |                              |
# | `assertIs(a, b)`          | `a is b`           | `a, b`            | Перевірка ідентичності       |
# | `assertIsNone(x)`         | `x is None`        | `x`               |                              |
# | `assertIn(a, b)`          | `a in b`           | `a, b`            |                              |
# | `assertRaises(exc)`       | Очікується виняток | `exc`             | Як контекст або функція      |

# Запуск тестів
# | Спосіб     | Приклад                       | Нюанс                      |
# | ---------- | ----------------------------- | -------------------------- |
# | Через файл | `python test_file.py`         | Потрібен `unittest.main()` |
# | Через CLI  | `python -m unittest`          | Автоматично шукає `test*`  |
# | Discovery  | `python -m unittest discover` | Шукає по папках            |

# Корисні фішки
# | Фіча            | Як використовується                | Нюанс                        |
# | --------------- | ---------------------------------- | ---------------------------- |
# | Пропуск тесту   | `@unittest.skip("reason")`         |                              |
# | Умовний skip    | `@unittest.skipIf(cond, "reason")` |                              |
# | Очікуваний фейл | `@unittest.expectedFailure`        |                              |
# | Subtests        | `with self.subTest(x=i):`          | Кілька кейсів в одному тесті |



class TestStringMethods(unittest.TestCase):
    # unittest.TestCase - Базовий клас для тестів. Усі тести мають наслідуватись від нього

    def setUp(self):
        """This doc string and list of tests will be displayed if test runs using key -v 
        python unit_test_038.py -v"""
        self.good_text = 'hello'
        self.bad_text = 'Goodbuy'
        self.no_text =''
        self.source = Source()
    

    def test_one(self):
        """AssertEqual"""
        # імена тестоих методів повинні починатись з test_ без цього тест не запуститься
        self.assertEqual(self.source.upper_text(self.good_text), "HELLO")

    def test_two(self):
        """AssertNotEqual"""
        self.assertNotEqual(self.source.upper_text(self.bad_text), "HELLO")    

    def test_tree(self):
        """AssertEndWith"""
        self.assertEndsWith(self.source.upper_text(self.bad_text), "BUY")    



if __name__ == '__main__':
    unittest.main()   
    # Запуск цього мейну обов'язковий для запуску тестів


