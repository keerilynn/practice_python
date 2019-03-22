import random

number = random.randint(1,5)

guess = int(input("Please enter a number between 1 and 5:    "))

while number != guess:
    guess = int(input("Not quite. Try another number between 1 and 5:     "))

if number == guess:
    print("You guessed it!")