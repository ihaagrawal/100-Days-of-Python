from data import menu
from data import resources

while resources['water']>=50 and resources['coffee']>=18:
    choice = input("What would you like to drink? espresso/latte/cappuccino: ")
    #espresso
    if choice == 'espresso' and menu['espresso']['ingredients']['water'] <=  resources['water'] and menu['espresso']['ingredients']['coffee'] <= resources['coffee']:
            print("That will be $1.50")
            
            quarters = int(input("No. of quarters: "))
            dime = int(input("No. of dimes: "))
            cents = int(input("No. of cents: "))
            penny = int(input("No. of pennies: "))

            paid = quarters*0.25 + dime*0.10 + cents*0.05 + penny*0.01
            
            if paid >= 1.50:
                change = paid - 1.50
                print(f"Your change is {round(change, 2)}")
                print("Enjoy your espresso.")
                resources['water'] -= 50
                resources['milk'] -= 0
                resources['coffee'] -= 18
            else:
                print("Money insufficient.")

    elif  menu['espresso']['ingredients']['water'] > resources['water']:
            print("Sorry! Water insufficient.")
    elif menu['espresso']['ingredients']['coffee'] > resources['coffee']:
            print("Sorry! Coffee insufficient.")

    #latte
    elif choice == 'latte' and menu['latte']['ingredients']['water'] <=  resources['water'] and menu['latte']['ingredients']['coffee'] <= resources['coffee'] and menu['latte']['ingredients']['milk'] <= resources['milk']:
  
            print("That will be $2.50")
            
            quarters = int(input("No. of quarters: "))
            dime = int(input("No. of dimes: "))
            cents = int(input("No. of cents: "))
            penny = int(input("No. of pennies: "))

            paid = quarters*0.25 + dime*0.10 + cents*0.05 + penny*0.01
            
            if paid >= 2.50:
                change = paid - 2.50
                print(f"Your change is {round(change, 2)}")
                print("Enjoy your latte.")
                resources['water'] -= 200
                resources['milk'] -= 150
                resources['coffee'] -= 24
            else:
                print("Money insufficient.")
        
    elif  menu['latte']['ingredients']['water'] > resources['water']:
            print("Sorry! Water insufficient.")
    elif  menu['latte']['ingredients']['coffee'] > resources['coffee']:
            print("Sorry! Coffee insufficient.")
    elif  menu['latte']['ingredients']['milk'] > resources['milk']:
            print("Sorry! Milk insufficient.")

    #cappucciono
    elif choice == 'cappuccino' and menu['cappuccino']['ingredients']['water'] <=  resources['water'] and menu['cappuccino']['ingredients']['coffee'] <= resources['coffee'] and menu['cappuccino']['ingredients']['milk'] <= resources['milk']:
            print("That will be $3.0")
            
            quarters = int(input("No. of quarters: "))
            dime = int(input("No. of dimes: "))
            cents = int(input("No. of cents: "))
            penny = int(input("No. of pennies: "))

            paid = quarters*0.25 + dime*0.10 + cents*0.05 + penny*0.01
            
            if paid >= 3.00:
                change = paid - 3.00
                print(f"Your change is {round(change, 2)}")
                print("Enjoy your cappuccino.")
                resources['water'] -= 250
                resources['milk'] -= 100
                resources['coffee'] -= 24
            else:
                print("Money insufficient.")
        
    elif  menu['cappuccino']['ingredients']['water'] > resources['water']:
            print("Sorry! Water insufficient.")
    elif  menu['cappuccino']['ingredients']['milk'] > resources['milk']:
            print("Sorry! Milk insufficient.")
    elif  menu['cappuccino']['ingredients']['coffee'] > resources['coffee']:
            print("Sorry! Coffee insufficient.")

    elif choice == 'report':
        print("Remaining resources: ")
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        exit

print("\n")
print("Sorry! No resources left anymore. Coffee Machine is turned off.")







