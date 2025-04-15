import random
rock = r'''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = r'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_paper_rock_scissors_game = [rock, paper, scissors]
player_of_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= player_of_choice <= 2:
    print(list_of_paper_rock_scissors_game[player_of_choice])

computer_choice = random.randint(0, 2)
print("Computer Chose:")
print(list_of_paper_rock_scissors_game[player_of_choice])

if player_of_choice >= 3 or player_of_choice < 0:
    print("You typed an invalid number. You lose!")
elif player_of_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_of_choice == 2:
    print("You lose!")
elif player_of_choice > computer_choice:
    print("You win!")
elif computer_choice > player_of_choice:
    print("You lose!")
elif player_of_choice == computer_choice:
    print("It's a draw.")