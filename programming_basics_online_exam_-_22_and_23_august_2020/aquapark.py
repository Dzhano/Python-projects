month = input() # "march", "april", "may", "june", "july" или "august"
hours = int(input())
people = int(input())
daytime = input() # "day" или "night"

if month == "march" or month == "april" or month == "may":
    if daytime == "day":
        price_per_hour_for_person = 10.50
    elif daytime == "night":
        price_per_hour_for_person = 8.4
elif month == "june" or month == "july" or month == "august":
    if daytime == "day":
        price_per_hour_for_person = 12.60
    elif daytime == "night":
        price_per_hour_for_person = 10.20
if people >= 4:
    price_per_hour_for_person *= 0.90
if hours >= 5:
    price_per_hour_for_person *= 0.50
total_price = price_per_hour_for_person * hours * people
print(f"Price per person for one hour: {price_per_hour_for_person:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")