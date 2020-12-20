budget = float(input())
counter = 0
total_price = 0
while True:
    command = input()
    if command == "Stop":
        print(f"You bought {counter} products for {total_price:.2f} leva.")
        break
    price = float(input())
    if price > budget:
        print("You don't have enough money!")
        print(f"You need {price - budget:.2f} leva!")
        break
    counter += 1
    if counter % 3 == 0:
        price /= 2
    budget -= price
    total_price += price