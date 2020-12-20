current = 1
n = int(input())
for row in range (1, n + 1):
    for col in range (1, row + 1):
        if current > n:
            exit()
        print(str(current), end=' ')
        current += 1
    print()