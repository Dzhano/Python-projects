budget = float(input())
laps = input() # "five" или "ten"
fan_card = input() # "yes" или "no"
type_kart = input()

if laps == "five":
    if type_kart == "Child":
        price = 7
    elif type_kart == "Junior":
        price = 9
    elif type_kart == "Adult":
        price = 12
    elif type_kart == "Profi":
        price = 18
elif laps == "ten":
    if type_kart == "Child":
        price = 11
    elif type_kart == "Junior":
        price = 16
    elif type_kart == "Adult":
        price = 21
    elif type_kart == "Profi":
        price = 32
if fan_card == "yes":
    price *= 0.80
elif fan_card == "no":
    price *= 1
if budget >= price:
    print(f"You bought {type_kart} ticket for {laps} laps. Your change is {(budget - price):.2f}lv.")
else:
    print(f"You don't have enough money! You need {(price - budget):.2f}lv more.")