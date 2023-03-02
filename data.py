def helloUser(name="Гость"):
    print(f"Привет {name}")


def printMax(a, b):
    res = ""
    if (a > b):
        res = f"{str(a)} больше {str(b)}"
    elif (a < b):
        res = f"{str(a)} меньше {str(b)}"
    elif (a == b):
        res = f"{str(a)} равняется {str(b)}"
    else:
        res = "Ошибка"
    print(res)


def inputInt():
    val = int(input("Введите число"))
    return val


def srSum():
    marks = [3, 5, 4]
    i = 0
    sum = 0
    while i <= len(marks) - 1:
        sum += marks[i]
        print(sum)
        i += 1
    sum /= len(marks)
    print(sum)

def sorti(list):
  list.sort()
  return list


def sum2(list):
    i = 0
    summ = 0
    while i <= len(list)-1:
        if(list[i]%2 == 0):
            print(list[i])
            summ += list[i]
        i+=1
    return summ


def createArr():
    arr = []
    coun = int(input("Введите желаемое количество элементов в списке: "))
    i = 0
    while i < coun:
        arr.append(int(input("Введите число: ")))
        i+=1
    print(arr)

