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
    time.sleep(2.3)
    print("A gaint dragon jumps out in front of you! He opens his jaws and... \n")
    time.sleep(1)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str()
