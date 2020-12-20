processor_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_numbers = int(input())
discount = float(input())

processor_price *= 1.57
video_card_price *= 1.57
ram_price *= 1.57
ram_price *= ram_numbers
processor_price -= processor_price * discount
video_card_price -= video_card_price * discount
total_price = processor_price + video_card_price + ram_price
print(f"Money needed - {total_price:.2f} leva.")