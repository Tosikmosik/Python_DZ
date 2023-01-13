# Вычислить число Пи c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

p = '3.1415926535897932384626433832795'

num = input()
count = 0
for i in range(len(num)):
    if num[i] == '0':
        count += 1

print(p[:count + 2])
#  Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

from random import randint as rnd

def dividers(a: int, uniq: bool = False) -> list[int]:
    i = 2
    dividers = []
    while a != 1:
        while a % i == 0:
            dividers.append(i)
            a //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers

a = int(input())
print(f'Список натуральных делителей числа {a}:{dividers(a)}')
print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')

# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

# Задана натуральная степень k. Сформировать
# случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. Даны два файла, в
# каждом из которых находится запись многочлена.

from functions import create_pol_file
from functions import create_polinom

k = int(input())

print(f'Сгенерированный полином {create_polinom(k)}')
print(f'Сгенерированный полином {create_polinom(k, False)}')
create_pol_file(create_polinom(k, 'new_file'))
