budget = int(input())
season = input()
people = int(input())
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if people <= 6:
    price *= 0.90
elif 7 <= people <= 11:
    price *= 0.85
elif people >= 12:
    price *= 0.75
if people % 2 == 0 and season != "Autumn":
    price *= 0.95
if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")