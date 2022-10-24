N = int(input("Введите год: "))
if (N % 400 == 0) or ((N % 4 == 0) and (N % 100 != 0)):
    print(False)
else:
    print(True)
