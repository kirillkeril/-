n1 = int(input("Ввдите n1: "))
n2 = int(input("Ввдите n2: "))

E = float(input("Введите Е: "))

b = [0]
for i in range(n1, n2):
    a = ((-1) ** (i-1)) / (i**i)
    if abs(a) >= E:
        b.append(a)
print(sum(b[:3]))