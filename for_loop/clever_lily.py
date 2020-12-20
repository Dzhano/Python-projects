age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
total_toy_money = 0
counter = 0
money = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        total_toy_money += toy_price
    else:
        money += counter + 10 - 1
        counter += 10
total_money = total_toy_money + money
if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - total_money:.2f}")