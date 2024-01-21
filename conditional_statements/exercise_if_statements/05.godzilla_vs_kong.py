budg_of_film = float(input())
statists_q = int(input())
outfit_price_per_statist = float(input())
decor = budg_of_film * 0.1

if statists_q > 150:
    outfit_price_per_statist *= 0.9

cost = statists_q*outfit_price_per_statist+decor

diff = abs(budg_of_film-cost)

if budg_of_film >= cost:
    print("Action!")
    print(f"Wingard starts filming with {diff:.02f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.02f} leva more.")
