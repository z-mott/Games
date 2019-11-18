

import numpy as np









dot = 'o '
centerdot = ' o'
money = 100
while money>0:
    num = raw_input("\n\nWhat outcome are you betting? (n to quit)\n")
    
    if num=='n':
        break
    try:
        num = int(num)
    except:
        print "Input must be an number(integer) try again. \n"
        continue
    if num<3 or num>18:
        print  "Input must be an from 3 to 18, try again.\n"
        continue
    bet = raw_input("How much are you betting?  You got " + str(money) + " dollars.\n")
    try: 
        bet = int(bet)
    except:  
        print "Bet must be a number (integer)"
        continue
    if  money<bet or bet < 0:
        print "You have " + str(money) +" dollar dude, be real.\n"
        continue

    ## up until this point is just input validation
### Below create the dice values and the acsii output
    values= np.random.randint(1,7,3)
    print(values)
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

    if num == sum(values):
        print "You win " +str(200*bet)+"\n"
        money = money + 200*bet
    else:
        print "You lose " + str(bet) +".\n"  
        money = money -bet





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