"""
Решение квадратного уравнения
"""

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0:
    print('Корней нет')

d = (b ** 2) - (4 * a * c)

if d < 0:
    print('Корней нет')
elif d > 0:
    x1 = int((-b + d ** 0.5) / (2 * a))
    x2 = int((-b - d ** 0.5) / (2 * a))
    print(x1, x2, sep='\n')
else:
    x = int(-b / 2 * a)
    print(x)
