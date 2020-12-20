best_score = 9999999999
best_name = ""
best_minutes = 0
best_seconds = 0
gold_cards = 0
silver_cards = 0
bronze_cards = 0
while True:
    name = input()
    if name == "Finish":
        break
    minutes = int(input())
    seconds = int(input())
    time = minutes * 60 + seconds
    if time < best_score:
        best_score = time
        best_name = name
        best_minutes = minutes
        best_seconds = seconds
    if time < 55:
        gold_cards += 1
    elif 85 >= time >= 55:
        silver_cards += 1
    elif 120 >= time > 85:
        bronze_cards += 1
print(f"With {best_minutes} minutes and {best_seconds} seconds {best_name} is the winner of the day!")
print(f"Today's prizes are {gold_cards} Gold {silver_cards} Silver and {bronze_cards} Bronze cards!")