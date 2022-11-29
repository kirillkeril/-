import math

def F(x):
    return math.tan(x/2) + 2 * math.cos(x)

a = float(input("Введите a: "))
b = float(input("Введите b: "))
h = float(input("Введите h: "))

i = a
while i <= b:
    r = F(i)
    print("|", i, "|", r, "|", '\n')
    i += h