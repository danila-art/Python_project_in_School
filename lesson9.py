import math
import random
# Задание 1


def mathHard(storona):
    dictKvadrat = {"Perimetr": 0, "Plochad": 0, "Diagonal": 0}
    dictKvadrat["Perimetr"] = storona*4
    dictKvadrat["Plochad"] = storona ** 2
    dictKvadrat["Diagonal"] = storona * math.sqrt(2)
    return dictKvadrat

# Задание 2


def numberMonth(number):
    if (number == 12 or number == 1 or number == 2):
        return "Зима"
    elif (number >= 3 and number <= 5):
        return "Весна"
    elif (number >= 6 and number <= 8):
        return "Лето"
    elif (number >= 9 and number <= 11):
        return "Осень"
    else:
        print("Число введено неккоретно")

# Задание 3


def yearHard(year):
    if (year % 4 == 0):
        return True
    else:
        return False

# Задание 4


def vkladBank(money, countYear):
    i = 1
    while i <= countYear:
        money += ((money/100)*10)
        i += 1
    return money

# задание 5


def game(userPos):
    arrPos = ["камень", "ножницы", "бумага"]
    totalBot = random.choice(arrPos)
    print(f"Ты поставил: {userPos}\nТвой противник поставил: {totalBot}")
    if (userPos == "камень"):
        if (totalBot == "камень"):
            print("Каша!")
        elif (totalBot == "ножницы"):
            print("Ура, ты выиграл!")
        elif (totalBot == "бумага"):
            print("Увы, ты проиграл!")
    elif (userPos == "ножницы"):
        if (totalBot == "камень"):
            print("Увы, ты проиграл!")
        elif (totalBot == "ножницы"):
            print("Каша!")
        elif (totalBot == "бумага"):
            print("Ура, ты выиграл!")
    elif (userPos == "бумага"):
        if (totalBot == "камень"):
            print("Ура, ты выиграл!")
        elif (totalBot == "ножницы"):
            print("Увы, ты проиграл!")
        elif (totalBot == "бумага"):
            print("Каша!")
    else:
        print("Вы ввели что-то неправильно! Попробуйте ещё раз!")
