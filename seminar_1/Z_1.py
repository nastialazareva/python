# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать m километров?

n = int(input("Введите километры за 1 день: "))
m = int(input("Введите количество километров за все время: "))

print((m+n-1)//n)
