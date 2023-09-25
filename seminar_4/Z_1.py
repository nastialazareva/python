# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется
# к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


my_list = "a a a b c a a d c d d".split()

print(my_list)

# Примечание:
# dict_1 = {1: 11, 2: 22, 3:33}
# print(list(dict_1)) - если преобразовать словарь в список, то мы получаем только ключи

dict_1 = {}

for letter in my_list[: - 1]:
    if letter in dict_1:
        dict_1[letter] += 1
        print(letter + "_" + str(dict_1[letter]), end = " ")
    else:
        dict_1[letter] = 0
        print(letter, end =" ")

if my_list[-1] in dict_1:
        dict_1[my_list[-1]] += 1
        print(my_list[-1] + "_" + str(dict_1[my_list[-1]]), end = " ")
else:
        dict_1[my_list[-1]] = 0
        print(my_list[- 1])