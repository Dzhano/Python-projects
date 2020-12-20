s = float(input())
months = int(input())

simple_beggining = s
complex_interest = s
for i in range (months):
    simple_interest = simple_beggining + 0.03 * s
    simple_beggining = simple_interest

    complex_interest = complex_interest + 0.027 * complex_interest
print(f"Simple interest rate: {simple_beggining:.2f} lv.")
print(f"Complex interest rate: {complex_interest:.2f} lv.")
if simple_beggining > complex_interest:
    print(f"Choose a simple interest rate. You will win {(simple_beggining - complex_interest):.2f} lv.")
elif simple_beggining < complex_interest:
    print(f"Choose a complex interest rate. You will win {(complex_interest - simple_beggining):.2f} lv.")