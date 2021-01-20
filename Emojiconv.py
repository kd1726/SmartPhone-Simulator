#!/usr/bin/env python
# coding: utf-8

# In[14]:


def emojiconv():
    emoji = True
    while emoji:
        print('If you want to leave the emoji converter, enter "quit". ')
        print('============================================================')
        type = input("What emoji do you want?").lower()
        emojis = {
            ":)":"😊",
            ":(":"☹",
            ":.(":"😥",
            ":D":"😁",
            "haha":"🤣",
            "ha":"😂",
            "ew":"🤢",
            ";)":"😉",
            "<3":"❤",
            "<3 <3":"💕"}
        if type == 'quit':
            break
        else:
            print(emojis[type])
emojiconv()

