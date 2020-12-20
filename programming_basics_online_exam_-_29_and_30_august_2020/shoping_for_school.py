a = int(input()) * 4.75
b = int(input()) * 1.80
c = int(input()) * 6.50
d = int(input()) * 2.50

total_price = a + b + c + d
total_price -= (total_price / 100) * 5
print(f"Your total is {total_price:.2f}lv")