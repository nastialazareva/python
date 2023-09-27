# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input = 5
# Output = yes

import random

def control(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


if control(int(input("Введите число: "))):
    print('Это простое число!')
else:
    print('Это составное число!')

    # random.randint(1, 101) 