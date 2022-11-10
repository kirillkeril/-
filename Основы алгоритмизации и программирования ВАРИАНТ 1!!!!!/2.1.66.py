print("Введите попарно точки прямоугольника начиная с левого верхнего угла через пробел")
(x1, y1) = list(map(int, input().split(' ')))
(x2, y2) = list(map(int, input().split(' ')))
(x3, y3) = list(map(int, input().split(' ')))
(x4, y4) = list(map(int, input().split(' ')))

if(
    abs(x1 - x2) == abs(x4 - x3) 
    or abs(y1 - y4) == abs(y2 - y3)
):
    x = float(input("Введите координату x точки "))
    y = float(input("Введите координату y точки "))

    if(
        (x1 < x and x < x2) and
        (y1 > y and y > y4)
    ):
        print("Точка принадлежит прямоугольнику")
    else: 
        print("Точка НЕ принадлежит прямоугольнику")
else:
    print("Это не прямоугольник".upper())
