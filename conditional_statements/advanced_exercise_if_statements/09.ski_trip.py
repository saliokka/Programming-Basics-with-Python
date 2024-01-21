days = int(input())
room_type = input()
review = input()
nights = days - 1
price_per_night = 0
total_price = 0

if room_type == "room for one person":
    price_per_night += 18.00
    total_price = price_per_night * nights

elif room_type == "apartment":
    price_per_night += 25.00
    total_price = price_per_night * nights

    if days < 10:
        total_price *= 0.70
    elif 10 <= days < 15:
        total_price *= 0.65
    elif days > 15:
        total_price *= 0.50

elif room_type == "president apartment":
    price_per_night += 35.00
    total_price = price_per_night * nights

    if days < 10:
        total_price *= 0.90
    elif 10 <= days < 15:
        total_price *= 0.85
    elif days > 15:
        total_price *= 0.80

if review == "positive":
    total_price *= 1.25
elif review == "negative":
    total_price *= 0.90

print(f"{total_price:.02f}")
