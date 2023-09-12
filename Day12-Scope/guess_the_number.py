import random
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Enter difficulty: hard or easy? ")

attempt_hard = 5
attempt_easy = 10

def hard():
    global attempt_hard
    if attempt_hard > 0:
        guess = int(input("Guess the number: "))
        if guess<number:
            attempt_hard -= 1
            print("Too low")
            print(f"You have {attempt_hard} attempts left.")
            hard()
        elif guess>number:
            attempt_hard -= 1
            print("Too high")
            print(f"You have {attempt_hard} attempts left.")
            hard()
        else:
            print("You guessed right. You win!")
            exit
    elif attempt_hard == 0:
        print("You ran out of attempts.")
        print("You lose.")
        exit

def easy():
    global attempt_easy
    if attempt_easy > 0:
        guess = int(input("Guess the number: "))
        if guess<number:
            attempt_easy -= 1
            print("Too low")
            print(f"You have {attempt_easy} attempts left.")
            easy()
        elif guess>number:
            attempt_easy -= 1
            print("Too high")
            print(f"You have {attempt_easy} attempts left.")
            easy()
        else:
            print("You guessed right. You win!")
            exit
    elif attempt_easy == 0:
        print("You ran out of attempts.")
        print("You lose.")
        exit
    
   
    
if difficulty == 'hard':
    hard()
else:
    easy()