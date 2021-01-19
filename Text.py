#!/usr/bin/env python
# coding: utf-8

# In[2]:


from twilio.rest import Client
account_sid ='ACc52255411661040dab50f0f944e722e5'
auth_token = '0b02b297eca7f0d64baa30f6993c1530'
#auth_token has been changed for security purposes
client = Client(account_sid, auth_token)
who = input("Enter the number that you would like to text: ")
msg = input('Type your message')
message = client.messages.create(
    to = who, 
    from_="+12188750645",
    body = msg)

print(message.sid)


# In[ ]:




