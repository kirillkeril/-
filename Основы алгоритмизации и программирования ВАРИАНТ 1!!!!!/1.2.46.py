import math
# Ввод переменных
print("Введите известные параметры треугольника ABC")

a = input("Сторона a: ")
b = input("Сторона b: ")
c = input("Сторона c: ")

(a,b,c) = (float(a),float(b),float(c))

# Вычисления и вывод
p = a+b+c
s = (0.5*p * (0.5*p-a) * (0.5*p-b) * (0.5*p-c))**0.5
C = math.degrees(math.asin((2*s) / (a*b)))
A = math.degrees(math.asin((2*s) / (c*b)))
B = math.degrees(math.asin((2*s) / (a*c)))
h = math.degrees(b / (1/math.tan(math.radians(a))))

print("Угол а: ", A, ", Угол b:" ,B, ", Угол c: ",C)
print("Периметр: ", p)
print("Площадь: ", s)
print("Высота: ", h)



    
