# Список с пользователями
arrUsersTotal = []

# Начальная функция


def countUser():
    countAddUser = int(
        input("Введите количество пользователей которые хотите добавить: "))
    if (countAddUser != 0):
        dictUser(countAddUser)
    else:
        print("Вы ввели нулевое значение, попробуйте ещё раз.")
        countUser()


# Итоговая функция
def arrUsers(dictUser, stop):
    if (dictUser and stop == "continue"):
        arrUsersTotal.append(dictUser)
        print("Новый пользователь добавлен!")
    elif (dictUser and stop == "stop"):
        arrUsersTotal.append(dictUser)
        print(arrUsersTotal)  # Доработать после проверки
        
# Промежуточная функция


def dictUser(count):
    for el in range(0, count):
        surname = input("Введите свою фамилию: ")
        name = input("Введите свое имя: ")
        age = input("Введите свой возраст: ")
        numberFhone = input("Введите свой номер телефона: ")
        thisDictUser = {"Surname": surname, "name": name,
                        "age": age, "numberFhone": numberFhone}
        if (el == count-1):
            print(f"el = {el} count = {count}")
            stop = "stop"
            arrUsers(thisDictUser, stop)
        else:
            print(f"el = {el} count = {count}")
            stop = "continue"
            arrUsers(thisDictUser, stop)


# второе задание в аудитории
def hardDict():
    date = {
        1: {
            "en": "Monday",
            "ru": "Понедельник"
        },
        2: {
            "en": "Tuesday",
            "ru": "Вторник"
        },
        3: {
            "en": "Wednesday",
            "ru": "Среда"
        },
        4: {
            "en": "Thursday",
            "ru": "Четверг"
        },
        5: {
            "en": "Friday",
            "ru": "Пятница"
        },
        6: {
            "en": "Saturday",
            "ru": "Суббота"
        },
        7: {
            "en": "Sunday",
            "ru": "Воскресенье"
        },
    }
    for e, val in date.items():
        print(f"Номер недели : {e}")
        for el, value in date[e].items():
            print(f"{el} : {value}")

