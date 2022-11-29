print("Введите попарно точки прямоугольника начиная с левого верхнего угла по часовой стрелке, вводя координаты через запятую")
(x1, y1) = list(map(float, input().replace(" ", '').split(',')))
(x2, y2) = list(map(float, input().replace(" ", '').split(',')))
(x3, y3) = list(map(float, input().replace(" ", '').split(',')))
(x4, y4) = list(map(float, input().replace(" ", '').split(',')))

print("Введите координаты точки А:", end=" ")
(xA, yA) = list(map(float, input().replace(" ", '').split(',')))

if (x1 == x4 and x2 and x3 and y1 == y2 and y3 == y4):
    if (xA > x1 and xA < x2):
        if (yA < y1 and yA > y4):
            print(True)
        else:
            print(False)
    else: 
        print(False)
else:
    print("Это не прямоугольник")