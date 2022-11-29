import math

x = float(input("Введите Х: "))
h = float(input("Введите шаг: "))
y = 2
while y <= 3:
    print(math.acos(y/x))
    y += h