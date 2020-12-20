number = float(input())
input_metric = input()
output_metric = input()
if input_metric == "m":
    if output_metric == "cm":
        number *= 100
    elif output_metric == "mm":
        number *= 1000
elif input_metric == "cm":
    if output_metric == "m":
        number /= 100
    elif output_metric == "mm":
        number *= 10
elif input_metric == "mm":
    if output_metric == "cm":
        number /= 10
    elif output_metric == "m":
        number /= 1000
print(f"{number:.3f}")