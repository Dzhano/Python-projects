type_flowers = input() # 'Roses', 'Dahlias', 'Tulips', 'Narcissus' или 'Gladiolus'
number_flowers = int(input())
budget = int(input())
if type_flowers == 'Roses':
    price = number_flowers * 5
    if number_flowers > 80:
        price *= 0.90
elif type_flowers == 'Dahlias':
    price = number_flowers * 3.80
    if number_flowers > 90:
        price *= 0.85
elif type_flowers == 'Tulips':
    price = number_flowers * 2.80
    if number_flowers > 80:
        price *= 0.85
elif type_flowers == 'Narcissus':
    price = number_flowers * 3
    if number_flowers < 120:
        price *= 1.15
elif type_flowers == 'Gladiolus':
    price = number_flowers * 2.50
    if number_flowers < 80:
        price *= 1.20
if budget >= price:
    print(f'Hey, you have a great garden with {number_flowers} {type_flowers} and {budget - price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price - budget:.2f} leva more.')