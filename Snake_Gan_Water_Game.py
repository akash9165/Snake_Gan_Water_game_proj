####Snake vs Water = win -> Snake
### Gan vs snake = win -> Gan
### Water vs Gane = win -> Water
import random
list_game = ["snake","gan","water"]
while 1:
    countUser=0
    countComputer =0
    choice1 =input('''
    -----------Welcome to snake gan water game--------
    1. Press 1 to start game
    2.Exit 2 
    ''')
    if choice1=='1':
        print("------Start the game-----")
        for i in range(1,6):
            user = int(input('''
            1.Snake
            2.Gan
            3.Water
            '''))
            if user==1:
                UserCo = "snake"
            elif user==2:
                UserCo = "gan"
            elif user==3:
                UserCo = "water"
            
            ComputerCho = random.choice(list_game)

            if UserCo==ComputerCho:
                print("Game draw")
                print("Your Choise is :- ",UserCo)
                print("Computer Choise is :- ",ComputerCho)
                countUser+=1
                countComputer+=1
            elif (UserCo=="snake" and ComputerCho=="water") or (UserCo=="gan" and ComputerCho=="snake") or (UserCo=="water" and ComputerCho=="gan"):
                print("--------You win-----------")
                print("Your Choise is :- ",UserCo)
                print("Computer Choise is :- ",ComputerCho)
                countUser+=1
            else:
                print("----Computer win-----")
                print("Your Choise is :- ",UserCo)
                print("Computer Choise is :- ",ComputerCho)
                countComputer+=1
        if countUser>countComputer:
                print("-------------Final Score is----------------")
                print("~~~~~~~~~~!!!~~~You Win~~~~~~!!!~~~~~~~~~~~~")
                print("Your score is :- ",countUser)
                print("Computer score is :- ",countComputer)
        elif countComputer>countUser:
                    print("-------------Final Score is----------------")
                    print("~~~~~~!!!~~~~~~~Computer Win~~~~~~~~!!!~~~~~~~~~~")
                    print("Your score is :- ",countUser)
                    print("Computer score is :- ",countComputer)
        else:
                print("-----------???-----Game draw-------???---------")
                print("Your score is :- ",countUser)
                print("Computer score is :- ",countComputer)
    else:
        break
