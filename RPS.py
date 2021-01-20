#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def Rock_Paper_Sissors_game():
    import random as r
    R = "R"
    P = "P"
    S = "S"
    z = [R,P,S]
    print('''
Rock - R
Paper - P
Sissors - S
Quit - Q
Help - H''') 
    R_P_S_says = input('Rock, Paper, Sissors, says:').upper()
    X = r.choice(z)
    while R_P_S_says != "Q":
        R_P_S_says = input('Rock, Paper, Sissors, says:').upper()
        if R_P_S_says == 'R':
            print(R_P_S_says)
            print(X)
            if r.choice(z) == 'P':
                print('Paper beats Rock. You lose!')
            elif r.choice(z) == "S":
                print('Rock beats Sissors. You win!')
            elif r.choice(z) =="R":
                print("Draw! Go again!")
        if R_P_S_says == 'P':
            print(R_P_S_says)
            print(X)
            if r.choice(z) == 'S':
                print('Sissors beats Paper. You lose!')
            elif r.choice(z) == "R":
                print('Paper beats Rock. You win!')
            elif r.choice(z) =="P":
                print("Draw, Go again!")
        if R_P_S_says == 'S':
            print(R_P_S_says)
            print(X)
            if r.choice(z) == 'P':
                print('Sissors beats Paper. You win!')
            elif r.choice(z) == "R":
                print('Rock beats Sissors. You lose!')
            elif r.choice(z) =="S":
                print("Draw, Go again!")
        if R_P_S_says =='H':
                print('''
    Rock - R
    Paper - P
    Sissors - S
    Quit - Q
    Help - H''')  
        elif R_P_S_says == 'Q':
            break
Rock_Paper_Sissors_game()

