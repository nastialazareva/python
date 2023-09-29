# "На вход программе подаются цифры, как только пользователь введет 0, ввод прекращается.
# Вывести наибольший элемент получившейся последовательности."
# Есть два кода с ошибками, нужно определить, где ошибок меньше.

# Ваня:
# n = int(input("Введите число: "))
# max_number = n # 1
# while n != 0:
#     if n > max_number: # 2
#        max_number = n
#     n = int(input("Введите еще одно число: ")) # 3
# print(f'Максимальное число в последовательности = {max_number}')

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

n = int(input())
max_number = n # или -1 (тоже можно)
while n > 0:  # 1
   if max_number < n:  
      max_number = n #2
   n = int(input())  # 3
print(max_number)   # 4