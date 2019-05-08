"""
Рисование лестницы из символов решетки и пробела
"""

import sys

steps = int(sys.argv[1])

for i in range(1, steps+1):
    spaces = steps - i
    sharps = steps - spaces
    print(' ' * spaces + '#' * sharps)
