"""
Сумма цифр в строке
"""

import sys

string = sys.argv[1]
print(sum([int(digit) for digit in string]))
