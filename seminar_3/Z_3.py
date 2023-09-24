# Напищшите программу для печати всх уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#         {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# Output: {'S005', 'S002', 'S007', 'S009'}
# Список словарей задан изначально. Пользовать его не вводит.



library= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
             {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

new_list = []

for cur_dict in library:
    for key in cur_dict:
        new_list.append(cur_dict[key])
        
print(f' Список всех значений ключй: {new_list}')
set_list = set(new_list)
print(f' Множество уникальных значений ключей: {set_list}')

# другой вариант
# set_list = set()

# for cur_dict in library:
#     for key in cur_dict:
#         set_list.add(cur_dict[key])

# print(set_list)