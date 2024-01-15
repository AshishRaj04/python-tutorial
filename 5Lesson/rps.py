import sys
import random
print(" ")

playerchoice = input("Enter... \n1 for Rock , \n2 for Paper , or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3 :
    sys.exit("you must enter 1 , 2 , 3")
    
comchoice = random.choice("123")

computer = int(comchoice)

print(" ")

print("You chose " + playerchoice + ".")
print("Com chose " + comchoice + ".")

print(" ")

if player == 1 and computer == 3:
    print("🥳 You won!")
elif player == 1 and computer == 2:
    print("👾 Com won!")
elif player == 2 and computer == 1:
    print("🥳 You won!")
elif player == 2 and computer == 3:
    print("👾 Com won!")
elif player == 3 and computer == 1:
    print("👾 Com won!")
elif player == 3 and computer == 2:
    print("🥳 You won!")
else :
    print("DRAW")