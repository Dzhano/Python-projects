name = input()
klass = 0
bad_grade = 0
total_grade = 0
while klass < 12:
    grade = float(input())
    total_grade += grade
    if grade < 4.00:
        bad_grade += 1
        if bad_grade > 1:
            klass += 1
            print(f"{name} has been excluded at {klass} grade")
            exit()
        continue
    klass += 1
average_grade = total_grade / klass
print(f"{name} graduated. Average grade: {average_grade:.2f}")