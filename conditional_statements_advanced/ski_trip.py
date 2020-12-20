days = int(input())
room = input() # room for one person, apartment или president apartment
rate = input() # positive или negative
nights = days - 1
if room == "room for one person":
    price = 18 * nights
elif room == "apartment":
    price = 25 * nights
    if 1 <= nights < 10:
        price *= 0.7
    elif 10 <= nights <= 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.5
elif room == "president apartment":
    price = 35 * nights
    if 1 <= nights < 10:
        price *= 0.9
    elif 10 <= nights <= 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.8
if rate == "positive":
    price *= 1.25
elif rate == "negative":
    price *= 0.9
print(f"{price:.2f}")