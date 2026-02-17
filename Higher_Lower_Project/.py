from game_data import data
import random
from art import *


def choice(list_data):
    num_data = random.choice(list_data)
    name = num_data['name']
    followers = num_data['follower_count']
    description = num_data['description']
    country = num_data['country']

    return name, description, country, followers
def choice_one(input_name):
    print(f"Compare {input_name[0]}, a {input_name[1]}, from {input_name[2]}")

def choice_two(input_name):
    print(f"Against {input_name[0]}, a {input_name[1]}, from {input_name[2]}")



def compare_choices(a, b, list_input):

    score = 0
    choice_one(a)
    print(vs)
    choice_two(b)

    while True:
        comparison = input("Who has more followers? A or B: ").lower()

        if comparison not in ["a", "b"]:
            print("Wrong input. Please type A or B.")
            choice_one(a)
            print(vs)
            choice_two(b)
            continue

        correct_answer = "a" if a[3] > b[3] else "b"

        if comparison == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}")
            a = b
            b = choice(list_input)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return

        choice_one(a)
        print(vs)
        choice_two(b)

def play_game():

    x = choice(data)
    y = choice(data)

    print(logo)

    compare_choices(x, y, data)

while input("Do you want to play the higher/Lower game? 'y'/'n'") == "y":
  play_game()


