print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip1 = total * (tip / 100)
total1 = total + tip1
amt = round(total1 / people, 2)
amt = "{:.2f}".format(amt)

print(f"Each person should pay: ${amt}")
