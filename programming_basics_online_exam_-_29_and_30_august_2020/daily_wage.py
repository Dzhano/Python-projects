rows = int(input())
positions = int(input())
strawberries = 0
bluberries = 0

for i in range(1, rows + 1):
    if i % 2 != 0:
        strawberries += positions
    else:
        for u in range(1, positions + 1):
            if u % 3 != 0:
                bluberries += 1
total_fruits = 3.50 * strawberries + 5 * bluberries
total_fruits *= 0.80
print(f"Total: {total_fruits:.2f} lv.")