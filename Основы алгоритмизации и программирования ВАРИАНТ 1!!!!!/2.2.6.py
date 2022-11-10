def F(x):
    if x <= 3:
        return x**2 - 3*x + 9
    if x > 3:
        return 1 / (x**3 + 6)

x = int(input("Введите x "))
print(F(x))