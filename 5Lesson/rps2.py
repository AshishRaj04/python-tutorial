import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playAgain = True

while playAgain:

    playerchoice = input(
        "\nEnter... \n1 for Rock , \n2 for Paper , or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("you must enter 1 , 2 , 3")

    comchoice = random.choice("123")

    computer = int(comchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Com chose " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3:
        print("🥳 You won!")
    elif player == 2 and computer == 1:
        print("🥳 You won!")
    elif player == 3 and computer == 2:
        print("🥳 You won!")
    elif player == computer:
        print("🥴 DRAW 😵")
    else:
        print("👾 Com won!😪")

    playAgain = input("\nPlay again? \nY for yes or \nQ to quit \n\n")
    if playAgain.lower() == "y":
        continue
    else:
        print("\n🍾🍾🍾🍾🍾\n")
        print("Thanks for playing")
        break
