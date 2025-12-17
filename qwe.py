import math

def f(x):
    return x**2 - math.sin(x) - 1

a = -3.0
b = 3.0
h = 0.2

x = a
count = 0

print(" x\t\tf(x)")
print("-" * 25)

a= x
f = f(x)

while x <= b:
    fx = f(x)
    print(f"{x:.1f}\t\t{fx:.5f}")

    if f * fx < 0:
        count += 1

    f = fx
    a = x
    x += h

print("\nКоличество корней на отрезке [-3; 3]:", count)
