# Есть код:
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")
# В переенную transformation нужно прописать такую функцию,чтобы в перемнной transformed_values получались
# копия списка values.


transformation = lambda x: x ** x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print("ok")
else:
    print("fail")

print(transformed_values)