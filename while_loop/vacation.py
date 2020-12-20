needed_money = float(input())
owned_money = float(input())
spend_days = 0
days = 0
while needed_money > owned_money:
    move = input()
    money = float(input())
    days += 1
    if move == "spend":
        owned_money -= money
        if owned_money < 0:
            owned_money = 0
        spend_days += 1
        if spend_days == 5:
            print("You can't save the money.")
            print(days)
            exit()
    elif move == "save":
        spend_days = 0
        owned_money += money
print(f"You saved the money for {days} days.")