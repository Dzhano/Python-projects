search = input()
book = input()
counter = 0
while book != search:
    counter += 1
    book = input()
    if book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter} books.")
        exit()
print(f"You checked {counter} books and found it.")