budget = int(input())
season = input()
fishermen_count = int(input())
boat_cost = 0

if season == "Spring":
    boat_cost += 3000
    if fishermen_count % 2 == 0:
        boat_cost *= 0.95
elif season == "Summer" or season == "Autumn":
    boat_cost += 4200
    if fishermen_count % 2 == 0 and season != "Autumn":
        boat_cost *= 0.95
elif season == "Winter":
    boat_cost += 2600
    if fishermen_count % 2 == 0:
        boat_cost *= 0.95

if fishermen_count <= 6:
    boat_cost *= 0.90
elif fishermen_count <= 11:
    boat_cost *= 0.85
else:
    boat_cost *= 0.75

diff = abs(budget-boat_cost)

if budget >= boat_cost:
    print(f"Yes! You have {diff:.02f} leva left.")
else:
    print(f"Not enough money! You need {diff:.02f} leva.")
