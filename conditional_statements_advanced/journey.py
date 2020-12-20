budget = float(input())
season = input()
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.30
        holiday = "Camp"
    elif season == "winter":
        budget *= 0.70
        holiday = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.40
        holiday = "Camp"
    elif season == "winter":
        budget *= 0.80
        holiday = "Hotel"
elif budget > 1000:
    destination = "Europe"
    budget *= 0.90
    holiday = "Hotel"
print(f"Somewhere in {destination}")
print(f"{holiday} - {budget:.2f}")