n = int(input())
divide2 = 0
divide3 = 0
divide4 = 0
for i in range (n):
    num = int(input())
    if num % 2 == 0:
        divide2 += 1
    if num % 3 == 0:
        divide3 += 1
    if num % 4 == 0:
        divide4 += 1
p2 = (divide2 * 100) / n
p3 = (divide3 * 100) / n
p4 = (divide4 * 100) / n
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")