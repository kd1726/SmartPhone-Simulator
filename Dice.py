#!/usr/bin/env python
# coding: utf-8

# In[10]:


print('''You can either put on or off as a command. 
If you say on, then you will roll the dice. Else, you
will exit the game.''')

def Dice():
    import random as r
    x = [1,2,3,4,5,6]
    a = r.choice(x)
    b = r.choice(x)
    return a,b

dice_on = input('Dice on or off?: ').lower

while dice_on != 'off':
    dice_on = input('Dice on or off?: ').lower()
    if dice_on == 'on': 
        Dice()
        print(Dice())
    elif dice_on =='off':
        print('See you later!')
        break


# In[ ]:




