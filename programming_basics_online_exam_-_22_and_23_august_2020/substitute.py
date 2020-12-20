k = int(input())
l = int(input())
m = int(input())
n = int(input())

changes = 0
for i in range(k, 9):
    for r in range(9, l - 1, -1):
        for t in range(m, 9):
            for u in range(9, n - 1, -1):
                if i % 2 == 0 and r % 2 != 0 and t % 2 == 0 and u % 2 != 0:
                    if i == t and r == u:
                        print("Cannot change the same player.")
                    else:
                        print(f"{i}{r} - {t}{u}")
                        changes += 1
                        if changes == 6:
                            exit()