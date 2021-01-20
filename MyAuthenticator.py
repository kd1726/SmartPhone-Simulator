#!/usr/bin/env python
# coding: utf-8

# In[1]:


Authenticate = True
def Authenticator():
    import random as r
    number_list = range(0,10)
    a = r.choice(number_list)
    b = r.choice(number_list)
    c = r.choice(number_list)
    d = r.choice(number_list)
    e = r.choice(number_list)
    f = r.choice(number_list)
    print([a,b,c,d,e,f])
while Authenticate:
    import time as t
    code = input("Would you like a code? If yes type 'Y' otherwise type 'N': ").upper()
    if code == 'Y':
        Authenticator()
        t.sleep(7)
    elif code =='N':
        break
    else:
        print('Invalid input')


# In[ ]:




