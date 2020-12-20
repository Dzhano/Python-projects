counter = 0
start = int(input())
end = int(input())
magic = int(input())
for a in range (start, end + 1):
    for b in range(start, end + 1):
        counter += 1
        if a + b == magic:
            print(f"Combination N:{counter} ({a} + {b} = {magic})")
            exit()
print(f"{counter} combinations - neither equals {magic}")