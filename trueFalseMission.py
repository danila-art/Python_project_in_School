# Условные операторы

def trashMain():
    mission1()
    mission2()
    mission3()
    mission4()
    mission5()
    mission6()


def mission1():
    print("Условные операторы ---- >   Запуск первого задания")
    num1 = int(input("Введите 1 число: "))
    num2 = int(input("Введите 2 число: "))
    if (num1 < num2):
        print(f"В данной ситуацией в стране:  число {num1} меньше чем {num2}")
    else:
        print(f"В данной ситуацией в стране:  число {num2} меньше чем {num1}")


def mission2():
    print("Условные операторы ---- >   Запуск второго задания")
    name = input("Введите свое имя: ")
    age = int(input("Введите свой возраст: "))
    if (age > 18):
        print(f"Добрый вечер, {name}! \n Вы совершеннолетний, поздравляем!")
    else:
        print(
            f"Привет, {name}!, Приносим извинения, но вы не можете гулять после 22:00")


def mission3():
    print("Условные операторы ---- >   Запуск третьего задания")
    num = int(input("Введите четырехзначное число: "))
    if (num > 1000):
        print("Успешно")
    else:
        print("Неудача")


def mission4():
    print("Условные операторы ---- >   Запус четвертого задания")
    dateOfBith = int(input("Введите номер месяца своего рождения: "))
    if (dateOfBith == 12 or dateOfBith == 1 or dateOfBith == 2):
        print("К холодам вам не привыкать")
    elif (dateOfBith >= 3 or dateOfBith <= 5):
        print("Подснежник")
    elif (dateOfBith >= 6 or dateOfBith <= 8):
        print("Вы родились летом")
    elif (dateOfBith >= 9 or dateOfBith <= 11):
        print("Я тоже люблю осенний листопад")
    else:
        print("Ошибка")


def mission5():
    print("Условные операторы ---- >   Запуск пятого задания")
    date = int(input("Введите год своего рождения: "))
    if (date % 4 == 0):
        if (date % 100 != 1 and date % 400 == 0):
            print("Вы случайно родились не 29 февраля?")
        else:
            print("Ошибочка, год не високосный")
    else:
        print("Ошибочка, год не високосный")


def mission6():
    print("Условные операторы ---- >   Запуск шестого задания")
    a = int(input("Введите значение стороны a"))
    b = int(input("Введите значение стороны b"))
    c = int(input("Введите значение стороны c"))
    if (a + b > c and a + c > b and b + c > a):
        print("Треугольник вроде адекватный")
    else:
        print("Треугольника с такими сторонами не существует")


