#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

print("Welcome to the Pizza Parlour!")
size = int(input("What size pizza would you like? 0 for Small, 1 for Medium and 2 for Large: "))
pep = input("Do you want Pepperoni? y or n: ")
cheese = input("Do you want Extra Cheese? y or n: ")

bill = 0

if size == 0:
    bill = 15
    if pep == 'y':
        bill += 2
    if cheese == 'y':
        bill += 1

elif size == 1:
    bill =20
    if pep == 'y':
        bill += 3
    if cheese == 'y':
        bill += 1

elif size == 2:
    bill = 25
    if pep == 'y':
        bill += 3
    if cheese == 'y':
        bill += 1

print(f"Your final bill is ${bill}")