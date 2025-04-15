from art import logo
import random
import os

# clear sceen
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Kart çekme fonksiyonu
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# calculater score
def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score

# winner
def compare(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score == computer_score:
        return "Draw 🙃"
    elif player_score == 21 and len(player_cards) == 2:
        return "Blackjack! You win 😎"
    elif computer_score == 21 and len(computer_cards) == 2:
        return "Computer has Blackjack! You lose 😱"
    elif player_score > computer_score:
        return "You win 😊"
    else:
        return "You lose 😤"

# game loop
def play_game():
    print(logo)

    # card list
    global player_cards, computer_cards
    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if player_score == 21 or computer_score == 21 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))


# main loop
while True:
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        clear()
        play_game()
    else:
        print("Goodbye! 👋")
        break
