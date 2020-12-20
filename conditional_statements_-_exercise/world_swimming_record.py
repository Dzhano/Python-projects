from math import floor
record = float(input())
meters = float(input())
time_meter = float(input())
time = meters * time_meter
extra_time = floor(meters / 15) * 12.5
total_time = time + extra_time
if record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record:.2f} seconds slower.")