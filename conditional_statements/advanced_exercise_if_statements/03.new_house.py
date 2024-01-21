type_of_flower = input()
flowers_quantity = int(input())
budget = float(input())
cost_per_flower = 0
total_cost = 0

if type_of_flower == "Roses":
    cost_per_flower = 5
    total_cost = cost_per_flower * flowers_quantity
    if flowers_quantity > 80:
        total_cost *= 0.90
elif type_of_flower == "Dahlias":
    cost_per_flower = 3.80
    total_cost = cost_per_flower * flowers_quantity
    if flowers_quantity > 90:
        total_cost *= 0.85
elif type_of_flower == "Tulips":
    cost_per_flower = 2.80
    total_cost = cost_per_flower * flowers_quantity
    if flowers_quantity > 80:
        total_cost *= 0.85
elif type_of_flower == "Narcissus":
    cost_per_flower = 3
    total_cost = cost_per_flower * flowers_quantity
    if flowers_quantity < 120:
        total_cost *= 1.15
elif type_of_flower == "Gladiolus":
    cost_per_flower = 2.50
    total_cost = cost_per_flower * flowers_quantity
    if flowers_quantity < 80:
        total_cost *= 1.20

diff = abs(budget-total_cost)

if budget >= total_cost:
    print(f"Hey, you have a great garden with {flowers_quantity} {type_of_flower} and {diff:.02f} leva left.")
else:
    print(f"Not enough money, you need {diff:.02f} leva more.")
