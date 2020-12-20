trip_price = float(input())
puzzles = int(input())
dolls = int(input())
teddies = int(input())
minions = int(input())
trucks = int(input())

price = puzzles * 2.60 + dolls * 3 + teddies * 4.10 + minions * 8.20 + trucks * 2
toys = puzzles + dolls + teddies + minions + trucks
if toys >= 50:
    price *= 0.75
rent = price * 0.10
price -= rent
if price >= trip_price:
    print(f"Yes! {price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - price:.2f} lv needed.")