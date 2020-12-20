n = int(input())
max_num = -9999999999999999
min_num = 9999999999999999
for i in range(n):
    number = int(input())
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")