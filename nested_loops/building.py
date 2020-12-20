levels = int(input())
rooms = int(input())
for a in range (levels, 0, -1):
    for b in range (rooms):
        if a == levels:
            print(f"L{a}{b}", end=" ")
        elif a % 2 == 0:
            print(f"O{a}{b}", end=" ")
        elif a % 2 != 0:
            print(f"A{a}{b}", end=" ")
    print()