people = int(input())
person_strenght = int(input())
illidan_blood = int(input())

power = people * person_strenght
if  power >= illidan_blood:
    print(f"Illidan has been slain! You defeated him with {power - illidan_blood} points.")
else:
    print(f"You are not prepared! You need {illidan_blood - power} more points.")