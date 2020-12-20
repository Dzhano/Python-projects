n = int(input())
max_num = -999999999
sum = 0
for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number
    sum += number
sum -= max_num
if sum == max_num:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {abs(sum - max_num)}")