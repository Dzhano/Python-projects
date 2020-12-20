exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

exam_minutes += exam_hour * 60
arriving_minutes += arriving_hour * 60
if exam_minutes == arriving_minutes:
    print("On time")
elif exam_minutes > arriving_minutes:
    if exam_minutes - arriving_minutes <= 30:
        print("On time")
        print(f"{exam_minutes - arriving_minutes} minutes before the start")
    elif 30 < exam_minutes - arriving_minutes <= 59:
        print("Early")
        print(f"{exam_minutes - arriving_minutes} minutes before the start")
    elif 60 <= exam_minutes - arriving_minutes <= 69 or 120 <= exam_minutes - arriving_minutes <= 129 or 180 <= exam_minutes - arriving_minutes <= 189 or 240 <= exam_minutes - arriving_minutes <= 249:
        extra_early_hours = (exam_minutes - arriving_minutes) // 60
        extra_early_minutes = (exam_minutes - arriving_minutes) % 60
        print("Early")
        print(f"{extra_early_hours}:0{extra_early_minutes} hours before the start")
    else:
        extra_early_hours = (exam_minutes - arriving_minutes) // 60
        extra_early_minutes = (exam_minutes - arriving_minutes) % 60
        print("Early")
        print(f"{extra_early_hours}:{extra_early_minutes} hours before the start")
elif exam_minutes < arriving_minutes:
    if arriving_minutes - exam_minutes <= 59:
        print("Late")
        print(f"{arriving_minutes - exam_minutes} minutes after the start")
    elif 60 <= arriving_minutes - exam_minutes <= 69 or 120 <= arriving_minutes - exam_minutes <= 129 or 180 <= arriving_minutes - exam_minutes <= 189 or 240 <= arriving_minutes - exam_minutes <= 249:
        extra_late_hours = (arriving_minutes - exam_minutes) // 60
        extra_late_minutes = (arriving_minutes - exam_minutes) % 60
        print("Late")
        print(f"{extra_late_hours}:0{extra_late_minutes} hours after the start")
    else:
        extra_late_hours = (arriving_minutes - exam_minutes) // 60
        extra_late_minutes = (arriving_minutes - exam_minutes) % 60
        print("Late")
        print(f"{extra_late_hours}:{extra_late_minutes} hours after the start")