prime_sum = 0
non_prime_sum = 0
while True:
    counter = 0
    command = input()
    if command == "stop":
        break
    num = int(command)
    if num < 0:
        print("Number is negative.")
        continue
    for i in range (1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2:
        non_prime_sum += num
    else:
        prime_sum += num
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")