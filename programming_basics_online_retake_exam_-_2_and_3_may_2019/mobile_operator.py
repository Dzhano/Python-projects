term = input() # "one" or "two"
type = input() # "Small", "Middle", "Large" or "ExtraLarge"
mobile_internet = input() # "yes" or "no"
months = int(input())
if term == "one":
    if type == "Small":
        price = 9.98
    elif type == "Middle":
        price = 18.99
    elif type == "Large":
        price = 25.98
    elif type == "ExtraLarge":
        price = 35.99
elif term == "two":
    if type == "Small":
        price = 8.58
    elif type == "Middle":
        price = 17.09
    elif type == "Large":
        price = 23.59
    elif type == "ExtraLarge":
        price = 31.79
if mobile_internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
elif mobile_internet == "no":
    price += 0
if term == "two":
    price -= price * 0.0375
price *= months
print(f"{price:.2f} lv.")