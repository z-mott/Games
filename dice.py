import random

value = random.randint(1,6)

print(value)

dot = 'o '
center = value%2

face = '\n---------\n| ' + dot[value<2] + '   ' + dot[value<4] + ' |\n| ' + dot[value<6] + ' '

print(face  + dot[center<1] + face[::-1])

"""
---------
| o   o |
|   o   |
| o   o |
---------

r=random.randrange(6)
C='o '
s='-----\n|'+C[r<1]+' '+C[r<3]+'|\n|'+C[r<5]
print(s+C[r&1]+s[::-1])

"""