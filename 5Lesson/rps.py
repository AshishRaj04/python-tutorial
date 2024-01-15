import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS.ROCK.value)
# print(RPS(2))


# sys.exit()
print(" ")

playerchoice = input(
    "Enter... \n1 for Rock , \n2 for Paper , or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("you must enter 1 , 2 , 3")

comchoice = random.choice("123")

computer = int(comchoice)

print(" ")

print("You chose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Com chose " + str(RPS(computer)).replace("RPS.", "") + ".")

print(" ")

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
