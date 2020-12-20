failed_threshold = int(input())
problems = 0
bad_counter = 0
total_score = 0
while True:
    command = input()
    if command == "Enough":
        break
    name = command
    grade = int(input())
    problems += 1
    total_score += grade
    if grade <= 4.00:
        bad_counter += 1
        if bad_counter == failed_threshold:
            print(f"You need a break, {bad_counter} poor grades.")
            exit()
average_score = total_score / problems
print(f"Average score: {average_score:.2f}")
print(f"Number of problems: {problems}")
print(f"Last problem: {name}")