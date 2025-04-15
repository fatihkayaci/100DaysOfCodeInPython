import random
from art import logo
def game(random_number, attempts):
    continue_game = True
    while continue_game:
        print(f"You have {attempts} attmpts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")
        elif guess == random_number:
            print(f"You got it! The answer was {random_number}")
            continue_game = False
        attempts -= 1
        if attempts == 0:
            continue_game = False
            print("You've run out of guesses. Refresh the page to run again.")
            
def easy_game(random_number):
    attempts = 10
    game(random_number, attempts)

def hard_game(random_number):
    attempts = 5
    game(random_number, attempts)

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100)
    choice_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice_difficulty == "easy":
        easy_game(random_number)
    elif choice_difficulty == "hard":
        hard_game(random_number)

print(logo)
play_game()

