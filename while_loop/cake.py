wedth = int(input())
length = int(input())
cake = wedth * length
command = input()
while command != "STOP":
    pieces = int(command)
    cake -= pieces
    if cake <= 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        exit()
    command = input()
print(f"{cake} pieces are left.")