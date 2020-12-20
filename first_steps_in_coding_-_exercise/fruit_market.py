strawberries_price_kilo = float(input())
bananas_kilo = float(input())
oranges_kilo = float(input())
raspberries_kilo = float(input())
strawberries_kilo = float(input())
raspberries_price_kilo = strawberries_price_kilo / 2
oranges_price_kilo = raspberries_price_kilo * 0.6
bananas_price_kilo = raspberries_price_kilo * 0.2
raspberries_price = raspberries_kilo * raspberries_price_kilo
oranges_price = oranges_kilo * oranges_price_kilo
bananas_price = bananas_kilo * bananas_price_kilo
strawberries_price = strawberries_kilo * strawberries_price_kilo
total_price = raspberries_price + bananas_price + oranges_price + strawberries_price
print(total_price)