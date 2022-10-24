x = float(input("Введите Х: "))
y = float(input("Введите Y: "))
r1 = 3
r2 = 5

if (x >= 0):
    if ((x**2 + y**2 >= r1**2) and (x**2 + y**2 <= r2**2)):
        print(True)
    else:
        print(False)
else: print(False)
