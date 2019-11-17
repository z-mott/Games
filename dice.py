

import numpy as np

values= np.random.randint(1,7,3)





print(values)

dot = 'o '
centerdot = ' o'

center = values%2
dicedash = '---------'
topline = '|' +dicedash + '|'  +  dicedash  + '|'  + dicedash  +  '|\n' 
line1 =  '|  ' + dot[values[0]<2] + '   ' + dot[values[0]<4] + '  |  ' \
        + dot[values[1]<2] + '   ' + dot[values[1]<4] + '  |  '\
        + dot[values[2]<2] + '   ' + dot[values[2]<4] + '  |\n'
line2 ='|  '+ centerdot[values[0]==6]+' ' + centerdot[values[0]%2] +' '+centerdot[values[0]==6]+'  '\
'|  '+ centerdot[values[1]==6]+' ' + centerdot[values[1]%2] +' '+ centerdot[values[1]==6]+'  |'\
'  '+ centerdot[values[2]==6]+' ' + centerdot[values[2]%2] +' '+ centerdot[values[2]==6]+'  |\n'
line3 =  '|  ' + dot[values[0]<4] + '   ' + dot[values[0]<2] + '  |  ' \
        + dot[values[1]<4] + '   ' + dot[values[1]<2] + '  |  '\
        + dot[values[2]<4] + '   ' + dot[values[2]<2] + '  |\n'
bottomline = topline



print('\n' +topline + line1 + line2+line3+bottomline)

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