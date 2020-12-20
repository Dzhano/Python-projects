count = int(input())
budget = int(input())
price = int(input())

tickets = count * price
if budget < tickets:
    print(f"The budget of {budget}$ is not enough. Your client can't buy {count} tickets with this budget!")
else:
    print(f"You can sell your client {count} tickets for the price of {tickets}$!")
    print(f"Your client should become a change of {budget - tickets}$!")