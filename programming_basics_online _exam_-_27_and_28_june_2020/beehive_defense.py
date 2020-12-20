bees = int(input())
bear_health = int(input())
bear_attack = int(input())
while True:
    bees -= bear_attack
    if bees < 100:
        if bees <= 0:
            print("The bear stole the honey! Bees left 0.")
        else:
            print(f"The bear stole the honey! Bees left {bees}.")
        break
    bear_health -= bees * 5
    if bear_health <= 0:
        print(f"Beehive won! Bees left {bees}.")
        break