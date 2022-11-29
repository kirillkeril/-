import math

n = int(input("Введите n: "))
k = int(input("Введите k: "))
a = []
for i in range(n):
    x = math.sin(i) + 3*math.cos(2*i)
    a.append(x)

print((a[:k]))