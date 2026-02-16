import random
import numpy as np

guess_list = np.arange(1, 101, 1)


def guess_num(guess_count, corr, guess):

    end_game = False

    while not end_game:

        guess_count -= 1

        if guess_count == 0:
            print("You Lost")
            end_game = True
            return

        if guess == corr:
            print("Correct! You win")
            return
        elif guess > corr:
            print("Guess lower")
        else:
            print("Guess higher")

        print(f"You have {guess_count} trials left")
        guess = int(input("Guess again: "))


def level(stage):
    if stage.lower() == "easy":
        return 5
    else:
        return 10


def play_game():
    print(r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
""")
    print("Welcome to the Guess Game")
    print("I'm thinking of a number from 1 to 100")
    difficulty_level = input("Choose a difficulty level: easy, hard: ")
    print(f"You have {level(difficulty_level)} trials")
    initial_guess = int(input("Guess the number: "))
    corr_number = random.choice(guess_list)
    guess_num(level(difficulty_level),corr_number, initial_guess)
    print("Thank you for playing this game")



while input("Do you want to play the numbers game? (y/n): ").lower() == "y":
    print("\n" * 30)
    play_game()





