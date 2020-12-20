n1 = int(input())
n2 = int(input())
operator = input()
if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        num = n1 + n2
    elif operator == "-":
        num = n1 - n2
    elif operator == "*":
        num = n1 * n2
    if num % 2 == 0:
        type = "even"
    else:
        type = "odd"
    print(f"{n1} {operator} {n2} = {num} - {type}")
elif (operator == "/" or operator == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")
elif operator == "/":
    num = n1 / n2
    print(f"{n1} {operator} {n2} = {num:.2f}")
elif operator == "%":
    num = n1 % n2
    print(f"{n1} {operator} {n2} = {num}")