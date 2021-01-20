#!/usr/bin/env python
# coding: utf-8

# In[154]:


#create game play fucntion
def start_game():
    global Game
    Game = True


# In[155]:


#build the board
global b
b = ["-","-","-","-","-","-","-","-","-"]
def board():
    print(b[0],"|",b[1],"|",b[2])
    print(b[3],"|",b[4],"|",b[5])
    print(b[6],"|",b[7],"|",b[8])
    return
board()


# In[156]:


#create the markers
def markers():
    markers = ['X',"O","1","2"]
    print('Marker Types')
    print('-------------')
    print(" ")
    print(markers)
    print(" ")
    print('-------------')
    global Game
    global player1
    global player2
    global marker2
    global marker1
    player1 = input('Player 1 input a name:')
    player2 = input('Player 2 input a name:')
    marker1 = input(f"{player1} which marker would you like").upper()
    marker2 = input(f"{player2} which marker would you like").upper()
    while marker1 and marker2 not in markers:
        if marker1 or marker2 not in markers:
            print('Not a valid marker. Please choose a valid marker')
            marker1 = input(f"{player1} which marker would you like").upper()
            marker2 = input(f"{player2} which marker would you like").upper()
            if marker1 and marker2 in markers:
                print(marker1)
                print(marker2)
                break
            else:
                ('Not a valid marker. Please choose a valid marker')
                marker1 = input(f"{player1} which marker would you like").upper()
                marker2 = input(f"{player2} which marker would you like").upper()
        else:
            print(marker1)
            print(marker2)
            break
    while marker1 !=marker2:
        if marker1 ==marker2:
            print('There cannot be two of the same markers')
            marker1 = input(f"{player1} which marker would you like").upper()
            marker2 = input(f"{player2} which marker would you like").upper()
        else:
            break
    go_on = input("Would you like to Continue? If No enter 'N',otherwise enter 'Y' or any input").upper()
    if go_on == "N":
        Game = False
        
    else:
        pass
    return


# In[174]:


def winner():
    global Game
    global tie
    row_win1 = b[0]==b[1]==b[2] != "-"
    row_win2 = b[3]==b[4]==b[5] != "-"
    row_win3 = b[6]==b[7]==b[8] != "-"
    col_win1 = b[0]==b[3]==b[6] != "-"
    col_win2 = b[1]==b[4]==b[7] != "-"
    col_win3 = b[2]==b[5]==b[8] != "-"
    diag_win1 = b[0]==b[4]==b[8] != "-"
    diag_win2 = b[2]==b[4]==b[6] != "-"
    tie = "-" not in b
    if row_win1 or row_win2 or row_win3:
        Game = False
        if row_win1:
            print("------------------------")
            print(b[0],"wins!")
            print("------------------------")
            Game = False
        elif row_win2:
            print("------------------------")
            print(b[3],"wins!")
            print("------------------------")
            Game = False
        elif row_win3:
            print("------------------------")
            print(b[6],"wins!")
            print("------------------------")
            Game = False
    elif col_win1 or col_win2 or col_win3:
        if col_win1:
            print("------------------------")
            print(b[0],"wins!")
            print("------------------------")
            Game = False
        elif col_win2:
            print("------------------------")
            print(b[1],"wins!")
            print("------------------------")
            Game = False
        elif col_win3:
            print("------------------------")
            print(b[2],"wins!")
            print("------------------------")
            Game = False
    elif diag_win1 or diag_win2:
        if diag_win1:
            print("------------------------")
            print(b[0],"wins!")
            print("------------------------")
            Game = False
        elif diag_win2:
            print("------------------------")
            print(b[2],"wins!")
            print("------------------------")
            Game = False
    elif tie:
        Game = False
        if "-" not in b:
            print("It's a tie!")
    else:
        Game = True
    return


# In[179]:


#turns and placement
def game_play():
    global Game
    global tie
    try:
        while Game:
            global position1
            global position2
            board()
            print(f"It is {player1}'s turn")
            position1 = int(input(f"{player1} please choose a position between 0-8"))
            if position1 not in [0,1,2,3,4,5,6,7,8,9]:
                print('This is an invalid input. Please put a valid input between 0-8')
            elif b[position1] != "-":
                while b[position1] != "-":
                    print('No no no, not today! HAHAHAHAHA!')
                    position1 = int(input(f"{player1} please choose a position between 0-8"))
                    if b[position1] == "-":
                        break
            b[position1] = marker1
            board()
            winner()
            print("If there is a tie with no more spot in enter and input enter 9")
            if b[position1] == marker1:
                print(f"It is {player2}'s turn")
            position2 = int(input(f"{player2} please choose a position between 0-8"))
            if position2 not in [0,1,2,3,4,5,6,7,8]:
                print('This is an invalid input. Please put a valid input between 0-8')
            elif b[position2] != "-":
                while b[position2] != "-":
                    print('No no no, not today! HAHAHAHAHA!')
                    position2 = int(input(f"{player2} please choose a position between 0-8"))
                    if b[position2] == "-":
                        break
            b[position2] = marker2
            board()
            winner()
            print("If there is a tie with no more spot in enter and input enter 9")
            go_on = input("Would you like to Continue? If No enter 'N',otherwise enter 'Y' or any other key but N").upper()
            if go_on == "N":
                Game = False
            elif go_on == "Y":
                pass
    except IndexError and ValueError:
        print("Not a valid input")
    return     


# In[183]:


def Game_on():
    print("""Welcome to Tic Tac Toe! The instructions on how to play will 
    be self explanitory as you play the game! If there is a tie 
    with no more spot in enter and input enter 9. If one enter's 
    '9' accidentally, please inquire that the other player enter 
    9 to maintain fairness.""")
    print("============================================================")
    start_game()
    global b
    b = ["-","-","-","-","-","-","-","-","-",'-']
    board()
    markers()
    while Game is True:
        game_play()

