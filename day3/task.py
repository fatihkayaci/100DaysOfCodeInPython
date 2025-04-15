print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island. \n Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice1 = input("Type \"left\" or \"right\" \n").lower()
if choice1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        choice3 = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("Eaten by beasts.\nGame Over.")
        elif choice3 == "red":
            print("Burned by fire.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("Fall into a hole.\nGame Over.")

