from game_data import data
from art import logo
from art import vs
import random


print(logo)

a = random.choice(data)
b = random.choice(data)


def choice(a, b):
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}. ")
  print(vs)
  print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.\n ")

choice(a, b)

score = 0

end_of_game = False

while end_of_game == False:
  answer = input("Who has more instagram followers: A or B? ")
  if a['follower_count'] > b['follower_count']:
    correct = 'A'
  elif a['follower_count'] > b['follower_count']:
    correct = 'B'
  elif a['follower_count'] == b['follower_count'] and answer == 'A':
    correct = 'A'
  else:
    correct = 'B'
  if answer == correct:
    score += 1
    print(f"Your score is {score}")
    a = b
    b = random.choice(data)
    choice(a, b)
  else:
    print("You answered wrong. Game ends.")
    print(f"Your score is {score}")
    end_of_game = True
  
   
    
    

