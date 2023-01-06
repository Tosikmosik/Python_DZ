# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = float(input())

while n % 1 != 0:
    n *= 10
print(n)
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
print(int(sum))
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input())
a = []
res = 1
for i in range(1, n + 1):
    res *= i
    a.append(res)
print(a)
# Задайте список из n чисел последовательности
# (1 + 1 / n)**n и выведите на экран их сумму.
# Пример: Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]


n = int(input())
sum = 0
a = []
for i in range(1, n + 1):
    a.append((1 + 1/i)** i)
    sum += (1 + 1/i)** i
print(a)
print(round(sum, 3)
# Реализуйте алгоритм перемешивания списка.

import random
n = list(map(int, input().split()))
print(n)

for i in range(len(n)):
    rand_pos = random.randint(- 1, len(n) - 1)
    n[i], n[rand_pos] = n[rand_pos], n[i]
print(n)
