import math
# Инициализация переменных
x = 0
y = 0
# Ввод переменных
x = int(input("Введите X: "))
y = int(input("Введите Y: "))
# Вычисления и вывод
res = x - (10**math.sin(x)) + math.cos(x-y)
print(res)
