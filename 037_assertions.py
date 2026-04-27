# Базовий синтакс 
# assert умова, [повідомлення про помилку]
# Якщо умова == False кидається ексепшн AssertionError

assert 2+2 == 4
# assert 2+2 == 5 #Just throw AssertionError
# assert 2+2 ==5, "Wrong equation" #Generate additional comment

def positive_multipliing(a, b):
    assert a > 0, 'a Parameter must be positive'
    assert b > 0, 'b Parameter must be positive'
    return a * b

try:
    print(positive_multipliing(5,3))
except AssertionError as e:
    print("catched negative parameter error: ", e  )

try:
    print(positive_multipliing(-5,3))
except AssertionError as e:
    print("catched negative parameter error: ", e  )

try:
    print(positive_multipliing(5,-3))
except AssertionError as e:
    print("catched negative parameter error: ", e  )        


# Assertions are being ignored in optimised mode which may be run as follows
#  python -O file.py
# This is criticcaly important if we are using assert for checking sensetive data
# НЕ використовуй для:
#  перевірки користувацького вводу
#  бізнес-логіки
#  критичних перевірок
# Замість цього краще вручну кидати ексепшн після if
