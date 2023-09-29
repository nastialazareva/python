# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)


def same_by(charcteristic, objects):
    result_list = list(filter(charcteristic, objects))
    print(result_list)

    if objects == result_list or result_list == []:
        return True
    return False

values = [5, 7, 9, 3]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")