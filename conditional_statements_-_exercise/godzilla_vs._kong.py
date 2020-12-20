budget = float(input())
statists_number = int(input())
statist_clothes = float(input())
decor = budget * 0.10
clothes_price = statist_clothes * statists_number
if statists_number > 150:
    clothes_price *= 0.90
total_price = clothes_price + decor
if total_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")