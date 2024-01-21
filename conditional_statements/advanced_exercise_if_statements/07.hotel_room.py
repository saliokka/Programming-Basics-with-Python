month = input()
nights = int(input())
price_for_studio = 0
price_for_apartment = 0


if month == "May" or month == "October":
    price_for_studio = 50
    price_for_apartment = 65
    if nights > 14:
        price_for_studio *= 0.70
    elif nights > 7:
        price_for_studio *= 0.95
elif month == "June" or month == "September":
    price_for_studio = 75.20
    price_for_apartment = 68.70
    if nights > 14:
        price_for_studio *= 0.80
elif month == "July" or month == "August":
    price_for_studio = 76
    price_for_apartment = 77

if nights > 14:
    price_for_apartment *= 0.90

print(f"Apartment: {price_for_apartment*nights:.02f} lv.")
print(f"Studio: {price_for_studio*nights:.02f} lv.")
