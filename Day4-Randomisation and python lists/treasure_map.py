row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

a = position[0]
b = position[1]

c = int(a)-1
d = int(b)-1

map[d][c]="X"
print(f"{row1}\n{row2}\n{row3}")
