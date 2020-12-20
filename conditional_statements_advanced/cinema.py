type = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
if type == "Premiere":
    income = capacity * 12
elif type == "Normal":
    income = capacity * 7.50
elif type == "Discount":
    income = capacity * 5
print(f"{income:.2f} leva")