#1 can covers 5 sq meters
import math
test_h = int(input("Enter height of wall: "))
test_w = int(input("Enter width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
    area = height * width
    paint = area/cover
    print(math.ceil(paint))
paint_calc(height=test_h, width=test_w, cover=coverage)