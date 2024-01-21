budget = float(input())
season = input()
reservation_place = " "
location = " "

if season == "summer":
    reservation_place = "Camp"
    if budget <= 100:
        budget *= 0.30
        location = "Bulgaria"
    elif budget <= 1000:
        budget *= 0.40
        location = "Balkans"
    else:
        budget *= 0.90
        location = "Europe"
        reservation_place = "Hotel"

elif season == "winter":
    reservation_place = "Hotel"
    if budget <= 100:
        budget *= 0.70
        location = "Bulgaria"
    elif budget <= 1000:
        budget *= 0.80
        location = "Balkans"
    else:
        budget *= 0.90
        location = "Europe"

print(f"Somewhere in {location}")
print(f"{reservation_place} - {budget:.02f}")
