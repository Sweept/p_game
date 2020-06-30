import random

guessesTaken = 0

print("Hello! What is your name?")
myName = input()

number = random.randint(1, 20)
guessBool = False
guessTries = 5
print("Welcome " + myName +
      ", to Guess a number from 1 to 20 game Made by Emerson Sridhar.")
print("Take a guess. You have a total of 5 guesses to find the correct number.")

for eachGuess in range(guessTries):
    print("You have {} remaining".format(guessTries - eachGuess))
    guess = input()
    guess = int(guess)
    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        print("You got it! The number was {}".format(number))
        guessBool = True
        guessesTaken = eachGuess + 1
        break

if guessBool == True:
    print("It took you {} out of {} guesses".format(guessesTaken, guessTries))
if guessBool == False:
    print("You've lost your 5 tries, the number was {}".format(number))
