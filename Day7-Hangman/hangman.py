import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo


chosen_word = random.choice(word_list)
length = len(chosen_word)

print(logo)

display = []
for i in range (0, length):
    display += "_"

end_of_game = False
lives = 6

while not end_of_game:
    guess = input("Guess a letter: ")

    if guess in display:
        print(f"You have already guessed {guess}")
    else:
        for i in range (0, length):
            if chosen_word[i] == guess:
                display[i] = guess
    
    if guess not in chosen_word:
        print("Letter not in word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            print(f"The word was: {chosen_word}")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win.")
        print(f"The word was: {chosen_word}")
    
    print(stages[lives])
