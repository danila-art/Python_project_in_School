def testOne():
    str = "Привет мир! Это тестовое сообщение для изучения."
    # print(str)
    # print(str.lower())
    # print(str.upper())
    # print(str.title())
    # print(str.capitalize())

    # str = str.split(' ')
    # print(str)
    # print(str.count("мир"))

    print(str.replace("Привет", "Hello"))


# Work1
def workOne(arr):
    for el in arr:
        print(f"{el}", end="\t")
    print()
# Work2


def workTwo(str):
    print(str[0:2])
    print(str[3:5])
    print(str[6::1])
# Work3


def workThree():
    strHello = "Hello, world!"
    strHello = strHello.replace('world', "мир!")
    print(strHello)
# Work4
def workFour():
    for el in range(1,11):
        print(el)


def factorial():
    numberUser = int(input("Введите число: "))
    fact = 1
    for num in range(fact, numberUser + 1):
        fact *=num
    return fact