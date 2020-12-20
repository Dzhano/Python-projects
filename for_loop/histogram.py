n = int(input())
p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0
for i in range(n):
    number = int(input())
    if number < 200:
        p1_counter += 1
    elif 200 <= number <= 399:
        p2_counter += 1
    elif 400 <= number <= 599:
        p3_counter += 1
    elif 600 <= number <= 799:
        p4_counter += 1
    elif number >= 800:
        p5_counter += 1
p1_procent = (p1_counter / n ) * 100
p2_procent = (p2_counter / n ) * 100
p3_procent = (p3_counter / n ) * 100
p4_procent = (p4_counter / n ) * 100
p5_procent = (p5_counter / n ) * 100
print(f"{p1_procent:.2f}%")
print(f"{p2_procent:.2f}%")
print(f"{p3_procent:.2f}%")
print(f"{p4_procent:.2f}%")
print(f"{p5_procent:.2f}%")