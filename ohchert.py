import math

a = 2
b = 5
n = int(input("Введите количество трапеций: "))
h = (b - a) / n
s = 0
for i in range(n + 1):
    x = a + i * h
    y = 1 / math.log(x)

    if i == 0 or i == n:
        s += y
    else:
        s += 2 * y
result = s * h / 2
print("Значение интеграла:", result)