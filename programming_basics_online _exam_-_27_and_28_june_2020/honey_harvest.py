flower = input() # "Sunflower", "Daisy", "Lavender", "Mint"
number_of_flowers = int(input())
season = input() # "Spring", "Summer", "Autumn"
if season == "Spring":
    if flower == "Sunflower":
        amount = 10
    elif flower == "Daisy":
        amount = 12
    elif flower == "Lavender":
        amount = 12
    elif flower == "Mint":
        amount = 10
elif season == "Summer":
    if flower == "Sunflower":
        amount = 8
    elif flower == "Daisy":
        amount = 8
    elif flower == "Lavender":
        amount = 8
    elif flower == "Mint":
        amount = 12
elif season == "Autumn":
    if flower == "Sunflower":
        amount = 12
    elif flower == "Daisy":
        amount = 6
    elif flower == "Lavender":
        amount = 6
    elif flower == "Mint":
        amount = 6
amount *= number_of_flowers
if season == "Summer":
    amount *= 1.10
elif season == "Autumn":
    amount *= 0.95
elif season == "Spring" and (flower == "Daisy" or flower == "Mint"):
    amount *= 1.10
print(f"Total honey harvested: {amount:.2f}")