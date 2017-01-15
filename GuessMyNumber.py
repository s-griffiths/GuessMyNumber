# GuessMyNumber.py
# User tries to guess computer's number

import random

# Random number is selected
randomNum = random.randint(1,1000)

print("I am thinking of a number between 1 and 1000, try and guess...")

guess = int(input("Enter a guess: "))

guessCount = 0

while guess != randomNum:
    if guess < randomNum:
        print("Higher")
        guessCount += 1
    elif guess > randomNum:
        print("Lower")
        guessCount += 1
    guess = int(input("Enter a guess: "))

print("You won! The number was " + str(guess) + ", it took you", guessCount, "guesses.")
        
