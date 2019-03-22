gamer_one = input("Welcome! What's your name?     ")
gamer_two = input("Hello to you too! What's your name?     ")

g1 = input("%s, Rock, paper, or scissors?     " % gamer_one)
g2 = input("%s, Rock, paper, or scissors?     " % gamer_two)

def game(g1, g2):
    if g1 == g2:
        return("It's a tie!")
    elif g1 == "rock":
        if g2 == "scissors":
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif g1 == "paper":
        if g2 == "rock":
            return("Paper wins!")
        else:
            return("Scissors wins!")
    elif g1 == "scissors":
        if g2 == "paper":
            return("Scissors wins!")
        else:
            return("Rock wins!")
    else:
        return("Oops. You did not enter rock, paper, or scissors correctly. Please try again.")

print(game(g1, g2))

