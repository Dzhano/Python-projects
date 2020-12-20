all_seats = 0
student_seats = 0
standard_seats = 0
kid_seats = 0
movie_name = input()
while movie_name != "Finish":
    taken_seats = 0
    counter = 0
    seats = int(input())
    type_seat = input()
    while type_seat != "End":
        counter += 1
        all_seats += 1
        taken_seats += 1
        if type_seat == "student":
            student_seats += 1
        elif type_seat == "standard":
            standard_seats += 1
        elif type_seat == "kid":
            kid_seats += 1
        if counter == seats:
            break
        type_seat = input()
    print(f"{movie_name} - {((counter * 100) / seats):.2f}% full.")
    movie_name = input()
print(f"Total tickets: {all_seats}")
print(f"{((student_seats * 100) / all_seats):.2f}% student tickets.")
print(f"{((standard_seats * 100) / all_seats):.2f}% standard tickets.")
print(f"{((kid_seats * 100) / all_seats):.2f}% kids tickets.")