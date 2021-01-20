#!/usr/bin/env python
# coding: utf-8

# In[25]:


def emailme1():
    import smtplib

    # Import the email modules we'll need
    import email
    from email.mime.text import MIMEText

    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = input("Message:")

    # me == the sender's email address
    # you == the recipient's email address
    #msg['Subject'] = 'The contents of %s' 
    Sender = input("Sender email:")
    Reciever = input("Reciever email:")


    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('127.0.0.1')
    s.sendmail(Sender, [Reciever], msg)
    s.quit()

def emailme2():
    import smtplib

    sender = input('Email of sender:')
    receiver = input('To which email would you like to send this messages')

    message = input("Message:")

    smtpObj = smtplib.SMTP('127.0.0.1')
    smtpObj.sendmail(sender, receiver, message)         
    print("Successfully sent email")

