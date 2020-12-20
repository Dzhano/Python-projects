total_steps = 0
while total_steps < 10000:
    command = input()
    if command == "Going home":
        steps = int(input())
        total_steps += steps
        break
    steps = int(command)
    total_steps += steps
if total_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - total_steps} more steps to reach goal.")