from math import floor
year = input()
p = int(input())
h = int(input())
city_games = ((48 - h) * 3) / 4
city_holidays_games = (p * 2) / 3
total_games = city_games + city_holidays_games + h
if year == "leap":
    total_games *= 1.15
print(floor(total_games))