# (Пользвательский ввод можно заменить на рандомный)
# Пользователь вводит натурльное число - k.
# В диапазоне от 0 до k нужно вывести все пары чисел N и M, в которых сумма делителей N
# равна M, а сумма делителе M равна N. (число само на себя делить нельзя).
# Пары необходимо выводит по одной паре в строке, разделяя числа пробелами.
# Каждая пара выводится только один раз, без повторов.


def sum_div(num):
    s = 1
    for div in range(1, int(num ** 0.5 + 1)):
        if num % div == 0:
            s += div + num // div
    return s

k = int(input("Введите число: "))
result = []

for first_num in range(2, k):
    second_num = sum_div(first_num)
    sum2 = sum_div(second_num)
    if first_num == sum2 and first_num != second_num:
            temp = (first_num, second_num)
            temp_result = min(temp), max(temp)
            if temp_result not in result:
               result.append(temp_result)

for i_tuple in result:
    print(*i_tuple)