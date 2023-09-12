import random
names = input("Enter names seperated by commas: ")
names = names.split(",")
#name is a list now

length = len(names)
rint = random.randint(0, length-1)
name = names[rint]

print(f"{name} will pay for the bill.")