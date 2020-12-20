from math import floor
income = float(input())
average_succees = float(input())
minimal_salary = float(input())

priceSS = minimal_salary * 0.35
priceSER = average_succees * 25
if income > minimal_salary:
    if average_succees < 5.50:
        print("You cannot get a scholarship!")
    else:
        print(f"You get a scholarship for excellent results {floor(priceSER)} BGN")
else:
    if average_succees < 5.50:
        print(f"You get a Social scholarship {floor(priceSS)} BGN")
    else:
        if priceSS > priceSER:
            print(f"You get a Social scholarship {floor(priceSS)} BGN")
        else:
            print(f"You get a scholarship for excellent results {floor(priceSER)} BGN")