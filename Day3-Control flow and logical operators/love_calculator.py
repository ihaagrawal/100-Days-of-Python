print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = (name1 + name2)
name_new = name.lower()

t = name_new.count('t')
r = name_new.count('r')
u = name_new.count('u')
e = name_new.count('e')

total_true = t+r+u+e

l = name_new.count('l')
o = name_new.count('o')
v = name_new.count('v')
e = name_new.count('e')

total_love = l+o+v+e



true = str(total_true)
love = str(total_love)

str_total = true + love

total = int(str_total)

if total<10 or total>90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total>40 and total<50:
    print(f"Your score is {total}, you are alright together."
)
else:
    print(f"Your score is {total}."
)
