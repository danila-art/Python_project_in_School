import lesson9


def goTolesson9():
    # вызов 1 задания
    num1 = int(input("Введите сторону квадарта: "))
    total1 = lesson9.mathHard(num1)
    print(total1)

    # вызов 2 задания
    num2 = int(input("Введите номер месяца: "))
    total2 = lesson9.numberMonth(num2)
    print(total2)
    # вызов 3 задания
    numYear = int(
        input("Введите год, который вы хотите проверить, високосный он или нет: "))
    total3 = lesson9.yearHard(numYear)
    print(f"Год високосный: {total3}")
    # вызов 4 задания
    numMoney = int(input("Введите сумму денег: "))
    numCountYear = int(
        input("Введите на сколько лет вы хотите сделть вклад: "))
    totalMoney = lesson9.vkladBank(numMoney, numCountYear)
    print(f"Твоя итоговая сумма: {totalMoney} руб.")

    # вызов 5 задания
    userPos = input(
        "Внимание Игра! Что вы выберете\n 1)камень\n2)ножницы\n3)бумага\nНапиши свой выбор: ")
    lesson9.game(userPos)
