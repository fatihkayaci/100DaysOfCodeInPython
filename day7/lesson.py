import random
words = ["at", "araba", "ev", "bilgisayar", "tamam"]
random_word = words[random.randint(0, len(words) - 1)]
random_word_lenght = len(random_word)
tip = ["_"] * random_word_lenght
healt = 6
game_over = False
while not game_over:
    demo = False
    print(f"6/{healt}")
    print(tip)
        
    user_input = input("Pleas enter char: ")
    i = 0
    for char in random_word:
        if char == user_input:
            tip[i] = char
            demo = True
        i += 1
    print(demo)
    if not demo:
        if healt > 0:
            healt -= 1
            
        if healt == 0:
            print("You lost")
            game_over = True