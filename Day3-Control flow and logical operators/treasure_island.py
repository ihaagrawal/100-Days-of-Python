print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

lr = input("You're at a cross road, where do you want to go? Type 'left' or 'right': ")
if lr == "left":
    sw = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")
    if sw == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?: ")
        if door == "blue":
            print("Eaten by beasts. Game over.")
        elif door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fell into a hole. Game Over.")
