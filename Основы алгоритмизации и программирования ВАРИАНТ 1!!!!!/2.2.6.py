def F(x):
    if x <= 7:
        return 3*x - 9
    if x > 3:
        return 1 / (x**2 - 4)

x = float(input("Введите x "))
print(F(x))