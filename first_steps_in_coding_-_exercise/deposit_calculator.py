deposit = float(input())
term = int(input())
year_procent = float(input())
deposit_price = deposit * (year_procent / 100)
deposit_month = deposit_price / 12
price = deposit + term * deposit_month
print(price)