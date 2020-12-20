days = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
cakes_price = cakes * 45
waffles_price = waffles * 5.80
pancakes_price = pancakes * 3.20
day_price = (cakes_price + waffles_price + pancakes_price) * bakers
campain_price = day_price * days
total_price = campain_price - campain_price / 8
print(total_price)