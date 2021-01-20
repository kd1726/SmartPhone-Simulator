#!/usr/bin/env python
# coding: utf-8

# In[8]:


def Guess_The_Sequence():
    guess = 1
    print('The sequence is 3 numbers long between 0-5')
    while guess != 10:
        guess = guess + 1
        sequence = input("What is the correct sequence")
        print('------------------------------------------------')
        if sequence == '341':
            print('You got it broski! Good job!')
            break
        elif  len(sequence) > 3:
            print('The sequence is only 3 numbers long')
        else:
            print('Not correct man, You got some tries left')
        if guess == 10:
            print('Sorry bro you lost')
            break
Guess_The_Sequence()


# In[ ]:




