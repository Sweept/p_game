import time
import random


def displayIntro():
    print("You are in a land full of dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight. \n")


def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave will you go into? (1 or 2)")
        cave = input()

    return cave


def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print("Its dark and spooky...")
    time.sleep(2)
    print("A gaint dragon jumps out in front of you! He opens his jaws and... \n")
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Gives you great wisdom and opportunity for the future, you leave the cave feeling strong!")
    else:
        print("The dragon attacks you! You fight back but you knew you can't beat him today, so you fled knowing you will return to this cave later...")


playAgain = 'yes'
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Do you want to play again? (yes or no)")
    playAgain = input()
