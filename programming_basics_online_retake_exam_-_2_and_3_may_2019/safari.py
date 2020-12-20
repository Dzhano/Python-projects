budget = float(input())
needed_fuel = float(input())
weekend_day = input() # "Saturday" or "Sunday"
fuel_price = needed_fuel * 2.10
complete = fuel_price + 100
if weekend_day == "Saturday":
    complete *= 0.9
elif weekend_day == "Sunday":
    complete *= 0.8
if budget >= complete:
    print(f"Safari time! Money left: {budget - complete:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {complete - budget:.2f} lv.")