n = int(input())
left_sum = 0
right_sum = 0
for i in range(n):
    number = int(input())
    left_sum += number
for j in range(n):
    right_number = int(input())
    right_sum += right_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")