#importing required files and libraries
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

#selecting a random word from word list
chosen_word = random.choice(word_list)
print(chosen_word)

#setting up lives and terminating condition
end_of_game = False
lives = 6

#printing logo
print(logo)

#list of blanks, no. of blanks = no. of letters in chosen word
display = []
for letter in chosen_word:
    display += "_"

#running a loop till game ends
length = len(chosen_word)
while end_of_game != True:

    #asking user to guess a letter
    guess = input("Guess a letter: ")

    #checking if guess is present in chosen word
    if guess in display:
        print("Already guessed.")
    else:
        for i in range(length):
            if guess == chosen_word[i]:
                display[i] = guess

    #if guess is wrong
    if guess not in chosen_word:
        print("Letter not in word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost.")
            print(f"The word was: {chosen_word}")

    print(f"Lives: {lives}")
    print(f"{' '.join(display)}")

    #if all the blanks are filled
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f"The word was: {chosen_word}")

    #printing ascii art depending on number of lives left
    print(stages[lives])



