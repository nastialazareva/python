# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# input: [1, 1, 2, 0, -1, 3, 4, 4]
# output: 6


myList = []

for i in range(5):
    myList.append(input('введите число: '))

    # другой вариант:
# size = int(input("Введите размер списка: "))
# for i in range(size):
#     myList.append(input('введите число: '))

mySet = set(myList)
print(*mySet)
print(len(mySet))