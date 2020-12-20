wedth = int(input())
lenght = int(input())
hight = int(input())
space = wedth * lenght * hight
command = input()
while command != "Done":
    boxes = int(command)
    space -= boxes
    if space <= 0:
        print(f"No more free space! You need {abs(space)} Cubic meters more.")
        exit()
    command = input()
print(f"{space} Cubic meters left.")