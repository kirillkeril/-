a = input("Введите четырехзначное число: ")
if len(a) == 4:
    s1 = int(a[0]) + int(a[1])
    s2 = int(a[-1]) + int(a[-2])
    print(s1 == s2)
else:
    print("Это не четырехзначное число.")
