bee = int(input())
flowers = int(input())
honey = bee * flowers * 0.21
honeycombs = honey // 100
left_honey = honey % 100
print(f"{honeycombs:.0f} honeycombs filled.")
print(f"{left_honey:.2f} grams of honey left.")