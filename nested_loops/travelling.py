destination = input()
while destination != "End":
    price = float(input())
    money = float(input())
    while money < price:
        money += float(input())
    print(f"Going to {destination}!")
    destination = input()