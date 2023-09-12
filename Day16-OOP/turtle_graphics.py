# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100.00)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()   

# table.field_names = ["Pokemon name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Bulbasaur", "Grass"],
#         ["Charmander", "Fire"],
#     ]
# )
# print(table)

table.add_column("Pokemon name", ["Starmie", "Onix", "Pigette"])
table.add_column("Type", ["Water", "Rock", "Bird"])
table.align = "l"

print(table)

