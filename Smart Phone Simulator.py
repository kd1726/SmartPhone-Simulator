#!/usr/bin/env python
# coding: utf-8

# In[1]:


def PhoneSoftware():
    import time
    power_on=True
    Decision = input("Would you like to power on your phone?").lower()
    while Decision =='yes':
        print("Power on!")
        print('--------------------------------------------------------')
        while power_on :
            print('''
    a - Call and text
    b - Games
    c - Miscellaneous
    d - Instructions
    e - Social media
    o - Power off''')
            What_to_do = input("What would you like to do? ").lower()
            print('--------------------------------------------------------')
            if What_to_do == "a":
                while What_to_do == "a":
                    print('''
                    a - call
                    b - text
                    q -leave call and text section
                    ''')
                    print('--------------------------------------------------------')
                    ask = input('Would you like to call or text? If not enter "q" to leave the app: ')
                    if ask == 'a':
                        import Call as c
                        c.call()
                        print('''
                        a - stay
                        b - leave''')
                        ask2 = input('Would you like to stay in the call section or leave?')
                        if ask2 == "a":
                            c.call()
                        if ask2 == 'b':
                            ask
                    elif ask == 'b':
                        import Text as t
                        print('''
                        a - stay
                        b - leave''')
                        ask2 = input('Would you like to stay in the texting section or leave?')
                        if ask2 == "a":
                            t.text()
                        if ask2 == 'b':
                            ask
                    elif ask =='q':
                        print('Leaving Call and Text Section...')
                        time.sleep(2)
                        break
                    else:
                        print("Invalid input or not software not supported.")

            elif What_to_do == "b":
                while What_to_do == "b":
                    print('''
            RPS - Rock Paper Sissors
            DG - Dice Game
            CG - Car Game
            GS - Guess the Sequence
            TTT - Tic Tac Toe
            Q - Leave game section
            ''')
                    print('--------------------------------------------------------')
                    if What_to_do == 'q':
                        break
                    else:
                        ask = input('Which game would you like to play').upper()
                        if ask =='RPS':
                            import RPS as rps
                            rps.Rock_Paper_Sissors_game()
                        elif ask =="DG":
                            import Dice as d
                            d.Dicey()
                        elif ask =="CG":
                            import Car_Game as cg
                            cg.Car_Game()
                        elif ask == "GS":
                            import Guess_the_Sequence_Game as gs
                            gs.Guess_The_Sequence()
                        elif ask == "TTT":
                            import Tic_Tac_Toe
                            from Tic_Tac_Toe import start_game,board,markers,winner,game_play,Game_on
                            global b
                            b = ["-","-","-","-","-","-","-","-","-",'-']
                            Game_on()
                        elif ask == 'Q':
                            print('Leaving Games...')
                            time.sleep(2)
                            break
                        else:
                            print('There is either an invalid input or the game is not supported.')

            elif What_to_do =="c":
                while What_to_do =="c":
                    print('''
                CV - Currency Converter
                EM - Email
                T - Translator
                GA - Google Authenticator
                M - Maps
                EC - Emoji Converter
                P - Photo
                Q - Leave miscellaneous section
                ''')
                    print('--------------------------------------------------------')
                    if What_to_do == 'q':
                        break
                    else:
                        ask = input('Which application would you like to use?').upper()
                        if ask == 'CV':
                            import Currencyconverter as cv
                            cv.Currency_Converter()
                        elif ask == 'EM':
                            import email_me
                            from email_me import emailme1,emailme2
                            print('''
                            It does not work due to the machine blocking the network connection, but
                            you can still input information.
                            Email styles:
                            a = emailme1
                            b = emailme2''')
                            style = input("which email style do you want?: ").lower()
                            if style == 'a':
                                emailme1()
                            elif style == "b":
                                emailme2()
                            else:
                                print('Not a valid input')
                        elif ask == 'T':
                            import Translationx
                            from Translationx import translate1,translate2
                            while ask == 'T':
                                print('''
                            If you would like to translate a text from english to a different language:
                            type "a" into the space provided.

                            If you would like to translate a foregin language into another foreign language
                            type "b" into the space provided

                            Enter "q" to leave the translator''')
                                translation_style = input("").lower()
                                if translation_style == 'a':
                                    translate1()
                                elif translation_style == 'b':
                                    translate2()
                                elif translation_style == 'q':
                                    print("Leaving Translation App...")
                                    time.sleep(2)
                                    break
                                else:
                                    print('Not a valid input')
                        elif ask == 'GA':
                            import MyAuthenticator as ma
                            ma.theauthenticator()
                        elif ask == 'M':
                            print('Need 300 dollars so it wont work. However you can input the information you want.')
                            import Mymaps as mm
                            mm.Mymaps()
                        elif ask == 'P':
                            import Screenshot as s
                            s.screenshots()
                        elif ask == 'EC':
                            import Emojiconv as ec
                            ec.emojiconv()
                        elif ask == 'Q':
                            time.sleep(2)
                            print('Leaving Miscellaneous...')
                            break
                        else:
                            print('There is either an invalid input or the application is not supported.')

            elif What_to_do == 'd':
                    print('''
                    Here are the commands to use the phone
        -----------------------------------------------------------------
                            a - Call and text
                            b - Games
                            c - Miscellaneous
                            d - Instructions
                            o - Power off ''')
                    print('--------------------------------------------------------')
            elif What_to_do == 'e':
                import Socialmedia
                from Socialmedia import SocialMedia as sm
                social_media =True
                while social_media:
                    print('You can go on any social media site you want. If you want to leabe enter "quit"')
                    which_one = input('Which social media do you want to use?').lower()
                    if which_one == 'quit':
                        social_media = False
                        print('Leaving Social Media...')
                        break
                    elif which_one == "facebook":
                        sm.Facebook()
                    elif which_one == "aol":
                        sm.Aol()
                    elif which_one == "youtube":
                        sm.Youtube()
                    elif which_one == "instagram":
                        sm.Instagram()
                    elif which_one == "twitter":
                        sm.Twitter()
                    elif which_one == "tiktok":
                        sm.Tiktok()
                    elif which_one == "tumblr":
                        sm.Tumblr()
                    elif which_one == "myspace":
                        sm.Myspace()
                    elif which_one == "snapchat":
                        sm.Snapchat()
                    elif which_one == "wattpad":
                        sm.Wattpad()
                    elif which_one == "wechat":
                        sm.Wechat()
                    elif which_one == "linkedin":
                        sm.LinkedIN()
                    elif which_one == "whatsapp":
                        sm.Whatapp()
                    elif which_one == "telegram":
                        sm.Telegram()
                    elif which_one == "gmail":
                        sm.Gmail()
                    elif which_one == "yahoo":
                        sm.Yahoo()
                    elif which_one == "google":
                        sm.Google()
                    elif which_one == "hotmail":
                        sm.Hotmail()
                    else:
                        print('Social Media Platform not supported!')
            elif What_to_do =="o":
                print('Power off...')
                power_on = False
                break
        break


# In[ ]:


PhoneSoftware()


# In[ ]:




