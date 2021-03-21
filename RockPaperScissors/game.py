from random import randint
import game_functions

# list of plays

plays = ["Rock", "Paper", "Scissors"]
# Computer picks a play from the list
computer = plays[randint(0,2)]


player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You Lose!", computer, "covers", player)
        else:
            print("You Win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose!", computer, "cuts", player)
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose!", computer, "smashes", player)
        else:
            print("You Win!", player, "cuts", computer)
    else:
        print("That is not a valid play. Check your spelling.")
    player = False
    computer = plays[randint(0,2)]