from art import logo, vs
from gamedata import data
import random
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#todo: against creator
def against_creator():
    datalength = len(data)
    against_random_number = random.randint(0, datalength - 1)
    against = data[against_random_number]
    return against

score = 0
compare = data[random.randint(0, len(data) - 1)]
death = False
while not death:
    clear()
    print(logo)
    if score >= 1:
        print(f"You're right! Current score: {score}")
        
    print(f"Compare A: {compare["name"]}, a {compare["description"]}, from {compare["country"]}")
    
    against = against_creator()
    
    print(vs)
    print(f"Againts B: {against["name"]}, a {against["description"]}, from {against["country"]}")

    player_choice = input("Who has more followers? Type 'A' or 'B': ")
    
    if player_choice.lower() == 'a' and (compare["follower_count"] > against["follower_count"]):
        score += 1
    elif player_choice.lower() == 'b' and (against["follower_count"] > compare["follower_count"]):
        score += 1
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        death = True
        
    compare = against
    
    