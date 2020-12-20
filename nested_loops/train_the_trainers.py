n = int(input())
total_average_grade = 0
grades = 0
presentation = input()
while presentation != "Finish":
    average_grade = 0
    for i in range(n):
        grade = float(input())
        average_grade += grade
        total_average_grade += grade
        grades += 1
    print(f"{presentation} - {(average_grade / n):.2f}.")
    presentation = input()
total_average_grade /= grades
print(f"Student's final assessment is {total_average_grade:.2f}.")