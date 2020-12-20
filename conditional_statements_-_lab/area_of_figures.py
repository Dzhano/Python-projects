import math
figure = input()
if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius * radius
elif figure == "triangle":
    side = float(input())
    hight = float(input())
    area = (side * hight) / 2
print(f"{area:.3f}")