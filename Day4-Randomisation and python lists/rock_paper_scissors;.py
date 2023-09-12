import random

print("Welcome to Rock, Paper, Scissors")
player = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors: "))

comp = random.randint(0,2)

if player == 0:
    print("You chose Rock.")
    if comp == 0:
        print("Computer chose Rock.")
        print("It's a tie.")
    elif comp == 1:
        print("Computer chose Paper.")
        print("You Lost.")
    else:
        print("Computer chose Scissors.")
        print("You Win.")

elif player == 1:
    print("You chose Paper.")
    if comp == 0:
        print("Computer chose Rock.")
        print("You Win.")
    elif comp == 1:
        print("Computer chose Paper.")
        print("It's a tie.")
    else:
        print("Computer chose Scissors.")
        print("You Lost.")
        
elif player == 2:
    print("You chose Scissors.")
    if comp == 0:
        print("Computer chose Rock.")
        print("You Lost.")
    elif comp == 1:
        print("Computer chose Paper.")
        print("You Win.")
    else:
        print("Computer chose Scissors.")
        print("It's a tie.")
