import random
HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'


def getRandomWord(wordList):
    wordList_Split = wordList.split()
    word_index = random.randint(0, len(wordList_Split) - 1)
    return wordList_Split[word_index]


def displayBoard(missedLetters, correctLetters, secretWord):
    # based on the number of missed letters, display approriate hangman pic
    print(HANGMAN_PICS[len(missedLetters)], "\n")
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            # Trick is here
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter")
        else:
            return guess


def playAgain():
    print("Do you want to play again? Y or N")
    return input().lower().startswith("y")


print("H A N G M A N")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    # Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Correct, the word is {}. You've won!".format(secretWord))
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You have run out of guesses!\nAfter {} missed guesses and {} correct guesses, the word was {}".format(
                str(len(missedLetters)), str(len(correctLetters)), secretWord))
            gameIsDone = True

# Ask the player if they want to play again if the game is ended
if gameIsDone:
    if playAgain():
        missedLetters = ''
        correctLetters = ''
        secretWord = getRandomWord(words)
        gameIsDone = False
    else:
        print("Thanks for playing Hangman")
