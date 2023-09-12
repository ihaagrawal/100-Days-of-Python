import random
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

start = input("Do you want to play the game? y or n: ")

if start == 'y':
    
    player_cards = []
    card1 = random.choice(values)
    card2 = random.choice(values)
    player_cards.append(card1)
    player_cards.append(card2)
    print(f"Your cards are {player_cards}.")
    player_score = card1 + card2
    print(f"Your score is {player_score}. ")

    computer_cards = []
    cc1 = random.choice(values)
    cc2 = random.choice(values)
    computer_cards.append(cc1)
    computer_cards.append(cc2)
    computer_score = cc1 + cc2
    print(f"Computer's first card is {cc1}")

else:
    print("Visit again.")
    exit()

def dealer_win(computer_cards, computer_score):
    print(f"Computer's final hand {computer_cards}")
    print(f"Computer's final score is {computer_score}")
    print("You Lose, Dealer Wins!")
    exit

def you_win(computer_cards, computer_score):
    print(f"Computer's final hand {computer_cards}")
    print(f"Computer's final score is {computer_score}")
    print("You win, Dealer lost!")
    exit

def ask_player(player_score, computer_score, player_cards, computer_cards):
    play = input("Type 'y' to get another card or 'n' to pass: ")
    if player_score<21 and computer_score<21:
        if play == 'y':
            pc = random.choice(values)
            player_cards.append(pc)
            player_score += pc
            print(player_cards)
            print(f"Your score is {player_score}")
        
            cc = random.choice(values)
            computer_cards.append(cc)
            computer_score += cc

        else:
            print(player_cards)
            print(f"Your score is {player_score}")

            cc = random.choice(values)
            computer_cards.append(cc)
            computer_score += cc
        
        if player_score>21 and computer_score<21:
            dealer_win(computer_cards, computer_score)
        elif player_score<21 and computer_score>21:
            you_win(computer_cards, computer_score)
        elif player_score==21 and computer_score != 21:
            you_win(computer_cards, computer_score)
        elif player_score!=21 and computer_score == 21:
            dealer_win(computer_cards, computer_score)    
        else:
            return ask_player(player_score, computer_score, player_cards, computer_cards)
        
ask_player(player_score, computer_score, player_cards, computer_cards)