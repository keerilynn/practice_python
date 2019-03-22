import random

roll = "Y"

while roll == "Y" or roll == "y":
    print(random.randint(1, 6))
    roll = input("Would you like to roll again? Y/N:     ")

    if roll == "N" or roll == "n":
        print("Thank you for playing.")