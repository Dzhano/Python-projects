days = 1
total_meters = 5364
while True:
    rest = input()
    if rest == "Yes":
        days += 1
    elif rest == "No":
        days += 0
    elif rest == "END":
        break
    if days > 5:
        break
    meters = int(input())
    total_meters += meters
    if total_meters >= 8848:
        print(f"Goal reached for {days} days!")
        break
if total_meters < 8848:
    print("Failed!")
    print(total_meters)