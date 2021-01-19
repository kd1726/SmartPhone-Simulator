#!/usr/bin/env python
# coding: utf-8

# In[22]:


#install audio manipulation package
#Create variables to hold the audio files
#add to while loop
def call():
    import playsound as ps
    from playsound import playsound as ps
    a = 'hear voice messages'
    b = 'make a call'
    c = 'view contacts'
    d = 'review call history'
    print('''
    a = hear voice messages
    b = make a call
    c = view contacts
    d = review call history
    any key = to leave the call app''')
    D = input("Would you like to hear voice messages, make a call, view contacts, or review call history: ").lower()
    print('----------------------------------------------------------------------------------------------')
    if D == 'a':
        print("Who's voice message would you like to hear?")
        print('')
        print('Kevin')
        print('Kevin Xu')
        print('Kevin Xi')
        print('Mom')
        print('Dennis')
        print('Dad')
        print('EJ')
        D1 = input("Who's voice message would you like to hear: ").lower()
        if D1 == 'kevin':
            ps('My-Voice-Message.mp3')
        elif D1 == 'dad':
            ps('Dad-Voice-Message.mp3')
        elif D1 == 'dennis':
            ps('Dennis-Voice-Message.mp3')
        elif D1 == 'mom':
            ps('Mom-Voice-Message.mp3')
        elif D1 == 'ej':
            ps('EJ-Voice-Message.mp3')
        elif D1 == 'kevin xu':
            ps('Kevin-Xu-Voice-Message.mp3')
        elif D1 == 'kevin xi':
            ps('Kevin-Xi-Voice-Message.mp3')
    else:
        pass
    if D == 'b':
        Contacts ={
            "kevin xu":"+16503536148",
            "ej":"+12408389899",
            "marielle zogheb":"+16093697913",
            "naana yawson":"+13476059287",
            "chris tsobze":"+13474449113",
            "chris tsobze home":"17188061153",
            "dad":"+13476531196",
            "mom":"+17183085410",
            "dennis doku":"+19293534276",
            "mike doku":"+233262760811",
            "home":"+17187602780"
        }
        print('''
    1     2     3
    
    4     5     5
    
    7     8     9
    
    *     #     #''')
        D4 = input('Dial Number: ').lower()
        if D4 == Contacts["kevin xu"]:
            print("Calling Kevin Xu...")
        if D4 == Contacts["ej"]:
            print("Calling EJ...")
        if D4 == Contacts["marielle zogheb"]:
            print("Calling Marielle Zogheb...")
        if D4 == Contacts["naana yawson"]:
            print("Calling Naana Yawson...")
        if D4 == Contacts["chris tsobze"]:
            print("Calling Chris Tsobze...")
        if D4 == Contacts["dad"]:
            print("Calling Precious Cargo...")
        if D4 == Contacts["mom"]:
            print("Calling Mom...")
        if D4 == Contacts["dennis doku"]:
            print("Calling Dennis Doku...")
        if D4 == Contacts["mike doku"]:
            print("Calling Mike Doku...")
            pass
        if D4 == Contacts["home"]:
            print("Calling Home...")
            pass
        else:
            D3 = input('This is an unknown contact. Would you like to add this number and person to your contact list').lower()
            if D3 == 'yes':
                D5 = input("'Name':'Number'")
                Contacts.get(D5)
                print(Contacts)
    if D == 'c':
        Contacts = [
            "Kevin Xu",
            "EJ",
            "Marielle Zogheb",
            "Naana Yawson",
            "Chris Tsobze",
            "Dad",
            "Mom",
            "Dennis Doku",
            "Mike Doku",
            "Home"
        ]
        print('''
    Contacts:
    
    Kevin Xu
    EJ
    Marielle Zogheb
    Naana Yawson
    Chris Tsobze
    Dad
    Mom
    Dennis Doku
    Mike Doku
    Home''')
        D2 = input('Which contact would you like to view: ').lower()
        if D2 == 'kevin xu':
            print('''
        Kevin Xu
        Mobile Number:+1 650 353 6148  ''')
        if D2 == 'ej':
            print('''
        EJ
        Mobile Number:+1 240 838 9899 ''')
        if D2 == 'marielle zogheb':
            print('''
            Marielle Zogheb
            Mobile Number: +1 609 369 7913 ''')
        if D2 == 'naana yawson':
            print('''
        Naana Yawson
        Mobile Number:+1 347 605 9287 ''')
        if D2 == 'chris tsobze':
            print('''
        Chris Tsobze
        Mobile Number:+1 347 444 9113
        Home Number: +1 718 806 1153''')
        if D2 == 'dad':
            print('''
        Precious Cargo
        Mobile Number:+1 347 653 1196 ''')
        if D2 == 'mom':
            print('''
        Mom
        Mobile Number:+1 718 308 5410 ''')
        if D2 == 'mike doku':
            print('''
        Mike Doku
        Mobile Number:+233 26 276 0811 ''')
        if D2 == "dennis doku":
            print('''
        Dennis Doku
        Mobile Number:+1 929 353 4276 ''')
        if D2 == 'home':
            print('''
            Home
            House Number: +1 718 760 2780''')
    if D == 'd':
        who = input("Who last called you?")
        list1 = ["Marielle","Kevin Xu","Mike"]
        list2 = list1.append(who)
        print(list1)
    else:
        print('I do not understand this input')
        
call()

# In[ ]:




