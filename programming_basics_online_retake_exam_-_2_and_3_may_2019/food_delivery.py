chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())
chicken_menus *= 10.35
fish_menus *= 12.40
vegetarian_menus *= 8.15
menus_price = chicken_menus + fish_menus + vegetarian_menus
dessert = menus_price * 0.2
total_price = menus_price + dessert + 2.50
print(f"Total: {total_price:.2f}")