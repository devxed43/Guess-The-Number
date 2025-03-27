# Edward Lopez
# March 27th, 2025
# CS 31
# Guess the number!

import random

# simply display game title
def display_title():
    print("Guess The Number Game!\n")

# Ask for player's name. Output their name at least once.
def get_name():
    player = input("what is your name?: ")
    print(f"Hello {player}!")

def play_game(wins, losses):
    # Ask player if they would like to play an EASY, MEDIUM or HARD game.
    mode = input("pick a game mode: \ne - easy: 1 to 10 \nm - medium: 1 to 100 \nh - hard: 1 to 1000: ")

    # if elif: if condition is true, apply the designated code block
    if mode.lower() == "e":
        LIMIT = 10
        TRIES = 5
    elif mode.lower() == "m":
        LIMIT = 100
        TRIES = 8
    elif mode.lower() == "h":
        LIMIT = 1000
        TRIES = 10
    else:
        print("Invalid input. Please pick a valid game mode")
        

    # ask user to enter a number for their guess
    target = random.randint(1, LIMIT)
    print(f"I'm thinking of a number between 1 and {LIMIT}\n")
    
    count = 1
    while count <= TRIES:
        guess = int(input("Your Guess: "))
        if guess < target:
            print("Your guess is too low")
        elif guess > target:
            print("Your guess is too high")
        elif guess == target:
            print("Ding! Ding! Ding!")
            wins += 1
            return wins, losses
        count += 1
    else:
        print(f"GAME OVER. the correct number was {target}")
        losses += 1
        return wins, losses
        


# control center for program. function names go in here
def main():
    display_title()
    get_name()
    wins = 0
    losses = 0
    again = "y"

    while again.lower() == "y":
        # this assigns wins and losses variables our new wins and losses inside of play game function
        wins, losses = play_game(wins, losses)
        print(f"wins: {wins} times\nlosses: {losses}")
        again = input("Wanna Play Again? (y/n): ")
    
    else:
        print("Thank you for playing. see ya around")

if __name__ == "__main__":
    main()










