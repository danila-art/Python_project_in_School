import data
import platform
import sys
import os
import module
import addUser
import completeLesson9
import mainConnection
# sec = int(input("Введите количество секунд: "))
# sec = sec % (24 * 60 * 60)
# hours = sec // 3600
# sec = sec % 3600
# min = sec // 60
# sec %= 60
# print(str(hours) + " часов " + str(min) + " минут " + str(sec) + " секунд")

# userPass = input("Введите пароль, для входа  в программу ")
# if (userPass == "password"):
#     num = int(input("Введите число: "))
#     numBool2 = None
#     numSymb = None
#     if ((num % 2) == 0):
#         numBool2 = True
#     else:
#         numBool2 = False
#     if (num >= 0 and num <= 9):
#         numSymb = True
#     else:
#         numSymb = False
#     print("Ваше число: " + str(num) + "! Четное: " +
#           str(numBool2) + " Однозначное: " + str(numSymb))
# else:
#     print("Вы неверное ввели пароль! Повторите попытку")

# if __name__ == "__main__":
#     def plus(a, b):
#         return a + b

#     def calc(a, b):
#         result = plus(a, b)
#         print(result)

#     def main():
#         a = int(input('Введите первое число'))
#         b = int(input('Введите второе число'))
#         calc(a, b)

#     main()

# Задание по циклам
# Задание 1
# num = 1
# while num <= 100:
#     print(f"{str(num)} ", end=", ")
#     num += 1
# print("\n")

# # Задание 2
# num2 = 1
# while num2 <= 100:
#     if (num2 % 5 == 0):
#         print(f"*{str(num2)}* ", end=", ")
#     else:
#         print(f"{str(num2)} ", end=", ")
#     num2 += 1

# print("\n")
# # Задание 3

# num3 = 0
# num4 = 1
# countNum = 1
# while countNum < 15:
#     num4 += num3
#     print(f"num4: {str(num4)} ", end="\t")
#     num3 = num4 - num3
#     countNum += 1

# fib = [0, 0, 1]
# while fib[0] < 15:
#     fib[2] = fib[2] + fib[1]
#     print(fib[2])
#     fib[1] = fib[2] - fib[1]
#     fib[0] += 1

# Функции


def main():
    # arr = [5, 10, 120, 30, 44, 56, 88, 92, 102, 103, 202, 66, 22]
    # # data.srSum()
    # sortiCom = data.sorti(arr)
    # print(sortiCom)
    # summa = data.sum2(arr)
    # print(summa)
    # data.createArr()
    # arr = ["str", 1, 6, 8, 9, True, 22, False]
    # module.workOne(arr)
    # dateOfBirthDay = "28:12:2000"
    # module.workTwo(dateOfBirthDay)
    # module.workThree()
    # module.workFour()
    # value = module.factorial()
    # print(value)
    # addUser.hardDict()
    # addUser.countUser()
    # completeLesson9.goTolesson9() #Проверочная работа
    trueFalseMission.trashMain()


if __name__ == "__main__":
    main()
