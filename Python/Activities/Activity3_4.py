while True:
    Player1 = input("Choose between Rock or Paper or scissors").lower()
    Player2 = input("Choose between Rock or Paper or scissors").lower()

if (Player1 == Player2):
    print("Its an tie")
elif Player1 == Rock:
    if Player2 == Scissors:
        print("Player 1 win")
    else:
        print("Player 2 win")
elif Player1 == Scissors:
    if Player2 == Paper:
        print("Player 1 win")
    else:
        print("Player 2 win")

elif Player1 == Paper:
    if Player2 == Rock:
        print("Player 1 win")
    else:
        print("Player 2 win")
repeat = "Do you want to continue Please type Yes or No"

if (repeat == 'Yes'):
    pass
elif(repeat == 'No'):
    exit
else:
    print("Invalid")

       



    