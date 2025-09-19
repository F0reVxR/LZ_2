import random
import math

"""
a = random.randint(10, 10000)
print(a)
"""
#First task
Length = int(17)
Width = float(19)
Square = Length * Width
print('Площадь участка', Square)

#Second task
Pi = math.pi
r = int(input('Введите радиус '))
Sq = Pi * (r^2)
Circ_Length = 2 * Pi * r
print('Площадь - ', Sq, 'Длина окружности - ', Circ_Length)

#Third task
a = float(input('Введите старший коэффициент '))
b = float(input('Введите средний коэффициент '))
c = float(input('Введите свободный коэффициент '))
