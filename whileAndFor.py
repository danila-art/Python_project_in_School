def mission1():
    print("Циклы ---- > Запуск первого задния")
    num1 = int(input('Введите 1 число: '))
    num2 = int(input('Введите 2 число: '))
    if(num1 > num2):
        while num1 > num2:
            if(num1 % 2 == 0):
                print(num1)
            num1 -= 1
    else:
        print("Первое чилсо должно быть больше второго, попробуйте еще раз.")
        mission1()

def mission2():
    print("Циклы ---- > Запуск второго задния")
    num = int(input("Введите число: "))
    while num != 0:
        num2 = int(input("Введите число: "))
        if(num2 != 0):
            num += num2
        else:
            break 
    print(f"Итоговое число: {num}")

def mission3():
    print("Циклы ---- > Запуск третьего задния")
    maxNum = 0
    while True:
        num = int(input("Введите число: "))
        if(num > maxNum):
            maxNum = num
        if(num == 0):
            break
    print(f"Ваше максимальное введеное число: {maxNum}")    

def mission4():
    
