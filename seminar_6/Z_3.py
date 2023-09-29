# (Пользвательский ввод можно заменить на рандомный)
# Пользователь вводит размер массива - N и его элементы (целые числа).print
# Нужно посчитать, сколько повторений у каждого числа.
# Посчитанные числа можно посчитать повторно в паре с другими числами.

from random import randint

def get_random_array(array_len: int) -> list[int]:
    """
    Получение случайного массива
    
    :param array_len: Размероность массива
    :return: Список цифр
    """
    return[randint(0, 9) for _ in range(array_len)]

def get_doubles(array: list[int]) -> int:
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                count += 1
    return count

if __name__ == "__main__":
    n = int(input("Введите размер массива: "))
    array = get_random_array(array_len = n)
    print(f'Массив: {array}')
    print(f'Количество повторений = {get_doubles(array=array)}')