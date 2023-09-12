auction = {}

def add_to_auction():
  key = input("Enter Name: ")
  value = int(input("Enter bid: $"))
  auction[key] = value

end_of_auction = False
add_to_auction()
check = input("Anymore bids (Y or N): ")


while end_of_auction == False:
  if check == 'Y' or check == 'y':
    add_to_auction()
    check = input("Anymore bids (Y or N): ")
    
  else:
    end_of_auction = True

max=0
for name in auction:
  if auction[name] > max:
    max = auction[name]
    winner = name
  else:
    continue

print(f"The winner is {winner} with the bid of ${max}")
    