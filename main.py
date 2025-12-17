import math

def f(x):
    return x**2 - math.sin(x) - 1

a = 1.0
b = 2.0

n = int(input("Введите количество итераций: "))

for i in range(n):
    c = (a + b) / 2

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

x = (a + b) / 2
print("Приближённый корень:", x)