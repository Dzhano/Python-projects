inteligence = int(input())
strong = int(input())
sex = input() # "female" or "male"
if inteligence >= 80:
    if strong >= 80:
        if sex == "female":
            print("Queen Bee")
        else:
            print("Repairing Bee")
    else:
        print("Repairing Bee")
elif inteligence >= 60:
    print("Cleaning Bee")
else:
    if strong >= 80:
        if sex == "male":
            print("Drone Bee")
        else:
            print("Worker Bee")
    elif strong >= 60:
        print("Guard Bee")
    else:
        print("Worker Bee")