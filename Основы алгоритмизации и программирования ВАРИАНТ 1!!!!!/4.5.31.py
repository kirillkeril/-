k = int(input("Введите k: "))

c = 0
s = 0
a = []
i = 0

inp = input("Введите число: ").replace(" ", '')
while inp != "":
    inp = int(inp)
    
    if (inp % 2 == 0):
        c += 1
    if (inp % k == 0):
        print("Кол-во четных чисел, введенных до числа, кратного k: ", c)
    
    if (inp > 0 and i != k):
        s += inp
        a.append(inp)
        i += 1
    if (i == k):
        r = 1
        for elem in a:
            r *= elem
        print("Среднее геометрическое превых k положительных чисел", r**0.5) 
    if (i == k):
        print("Сумма первых k положительных чисел: ", s)
    
    inp = input("Введите число: ").replace(' ', '')

