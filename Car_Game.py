#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Car_Game():
    print('''
    start - to start the car
    stop - to stop the car
    help - to learn how to play
    quit - to quit
    input the stop command twice, then start to start the car''')
    print('--------------------------------------------')
    command = input("Give command: ").lower()
    started = True
    travel = True
    while command.lower() != "quit":
        command = input("Give command: ").lower()
        print('--------------------------------------------')
        if command == "start":
            if started:
                print('You have already started the car!')
            else:
                started =True
                print('Car has started...')
                travel = True
                while travel:
                    print('''
                    North
                    South
                    East
                    West''')
                    ask = input('Which direction would you like to go: ').lower()
                    query = input('Coninute? If yes, type y, if no type n').lower()
                    print('--------------------------------------------')
                    if ask == 'north' and query == 'y':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                    elif ask == 'north' and query == 'n':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                        break
                    elif ask == 'west' and query == 'y': 
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                    elif ask == 'west' and query == 'n':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                        break
                    elif ask == 'east' and query == 'y':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                    elif ask == 'east' and query == 'n':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                        break
                    elif ask == 'south' and query == 'y':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                    elif ask == 'south' and query == 'n':
                        ask2 = int(input('How many kilometers:'))
                        print(f'You drove',ask2,f'kilometers',ask)
                        break
                    else:
                        print("I'm sorry I don't understand this input")
        elif command == "stop":
            print("Car has stopped!")
            if not started:
                print("You have already stopped the car!")
            else:
                started = False
                travel = False
                print("Car has stopped!")
        elif command == "help":
            print('''
    start - to start the car
    stop - to stop the car
    Help"
    Quit''')
        elif command =="quit":
            break
        else:
            print("I don't understand this")
Car_Game()


# In[ ]:




