# Напишите программу, которая принимает на вход
# цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
#
# Пример:
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет
num = int(input("Введите число от 1 до 7: "))
if num <= 5:
    print("Будни")
elif num >= 8:
    print("введите число от 1 до 7")
else:
    print("выходной")

# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")


    # Напишите программу, которая принимает на вход координаты точки
    # (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
    # в которой находится эта точка (или на какой оси она находится).

    def inputKoord(x):
        a = [0] * x
        for i in range(x):
            is_OK = False
            while not is_OK:
                try:
                    number = float(input(f"Введите {i + 1} координату: "))
                    a[i] = number
                    is_OK = True
                    if a[i] == 0:
                        is_OK = False
                        print("Координата не должно быть равна 0 ")
                except ValueError:
                    print("Ты ошибся. Вводить надо числа!")
        return a


    def checkCoordinates(xy):
        text = 4
        if xy[0] > 0 and xy[1] > 0:
            text = 1
        elif xy[0] < 0 and xy[1] > 0:
            text = 2
        elif xy[0] < 0 and xy[1] < 0:
            text = 3
        print(f"Точка находится в {text} четверти плоскости")


    koordinate = inputKoord(2)
    checkCoordinates(koordinate)


    # Напишите программу, которая по заданному номеру
    # четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

    def inputNumbers(x):
        xy = ["X", "Y"]
        a = []
        for i in range(x):
            is_OK = False
            while not is_OK:
                try:
                    number = int(input(f"Введите координату по {xy[i]}: "))
                    a.append(number)
                    is_OK = True
                except ValueError:
                    print("Ты ошибся. Вводить надо целые числа!")
        return a


    def calculateLengthSegment(a, b):
        lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
        return lengthSegment


    print("Введите координаты точки А")
    pointA = inputNumbers(2)
    print("Введите координаты точки В")
    pointB = inputNumbers(2)

    print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")


