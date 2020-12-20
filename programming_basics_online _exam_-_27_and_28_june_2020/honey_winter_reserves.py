winter_honey = float(input())
total_honey = 0
name = input()
while name != "Winter has come":
    bee_honey = 0
    for i in range (6):
        honey = float(input())
        bee_honey += honey
    total_honey += bee_honey
    if bee_honey < 0:
        print(f"{name} was banished for gluttony")
    if total_honey >= winter_honey:
        print(f"Well done! Honey surplus {(total_honey - winter_honey):.2f}.")
        exit()
    name = input()
if total_honey >= winter_honey:
    print(f"Well done! Honey surplus {(total_honey - winter_honey):.2f}.")
else:
    print(f"Hard Winter! Honey needed {(winter_honey - total_honey):.2f}.")