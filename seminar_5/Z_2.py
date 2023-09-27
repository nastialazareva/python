# Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# минимальные оценки на  максимальные. Напишите программу, которая заменяет
# оценки Василия, но наоборот: все максимальные – на минимальные.
# Input = 5 -> 1 3 3 3 4
# Output = 1 3 3 3 1


import random

def find_min_max(lst):
    min_num = lst[0]
    max_num = lst[0]
    for num in lst[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

def change_num(min_n, max_n, lst):
    for i in range(len(lst)):
        if lst[i] == max_n:
            lst[i] = min_n
    return lst

n = 5
list_1 = [random.randint(1, 5) for _ in range(n)]

# min_num = min(list_1)
# max_num = max(list_1)
min_num, max_num = find_min_max(list_1)
print(list_1)
print(change_num(min_num, max_num, list_1))
