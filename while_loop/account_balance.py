sum = 0
while True:
    command = input()
    if command == "NoMoreMoney":
        break
    money = float(command)
    if money < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {money:.2f}")
    sum += money
print(f"Total: {sum:.2f}")