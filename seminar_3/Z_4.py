# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером).
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)


my_list = []
size = int(input("Введите размер массива: "))
count = 0

for _ in range(size):
    my_list.append(input("Введите число: "))

print(f'Массив = {my_list}')

for i in range(size - 1):
    if my_list[i] < my_list[i + 1]:
        count += 1

print(f'Количество элементов массива, больших предыдущего: {count}')


# ВАРИАНТ 2:

# res_list_1 = [my_list[i + 1] for i in range(size - 1) if my_list[i] < my_list[i + 1]]
# --если без else, то if ставится после for

# res_list_2 = [my_list[i + 1] if my_list[i] < my_list[i + 1] else 0 for i in range(size - 1)] -- если
# есть блок else, то if ставится перед for (между выражением и for)

# print(res_list_1)
# print(res_list_2)