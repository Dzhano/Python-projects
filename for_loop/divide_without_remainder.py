n = int(input())
p2_counter = 0
p3_counter = 0
p4_counter = 0
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        p2_counter += 1
    if number % 3 == 0:
        p3_counter += 1
    if number % 4 == 0:
        p4_counter += 1
p2_procent = (p2_counter / n ) * 100
p3_procent = (p3_counter / n ) * 100
p4_procent = (p4_counter / n ) * 100
print(f"{p2_procent:.2f}%")
print(f"{p3_procent:.2f}%")
print(f"{p4_procent:.2f}%")