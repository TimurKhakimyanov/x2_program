#code for calculating the roots of a square equation
#arguments are entered in the order a then enter and then enter and C then enter
#Used only for calculation of full quadratic equations
#June 2020

#код для вычисления корней квадратного урованения
#аргументы вводятся в порядке a потом enter и потом enter и с потом enter
#Используется только для вычисления полных квадратных уравнений 
#Июнь 2020


from math import sqrt
a = 0
b = 0
c = 0
d = 0
x1 = 0
x2 = 0

a = int(input())
b = int(input())
c = int(input())

d = (b*b)-(4*a*c)
print("дискриминант равен",d)

if d == 0:
    x1 = (-b+d)/(2*a)
    print("первый корень равен",x1)
if d > 0:
    d = pow(d,0.5)
    print("корень из дискриминанта" , d)  
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    print("первый корень",x1)
    print("второй корень",x2)
if d < 0:
    print("нет решения")
