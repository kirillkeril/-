A = int(input('Введите A: '))
B = int(input('Введите B: '))
C = int(input('Введите C: '))
time = int(input('Введите суммарное время разговоров за месяц: '))

if(time < 0 or A <= 0 or B <= 0 or C <= 0):
    print("Введены неверные данные")
else:
    res = 0

    if time <= A:
        res = B
        print("Плата составила ", res, " рублей")
    else:
        res = B + C * (time - A)
        print("Плата составила ", res, " рублей")
