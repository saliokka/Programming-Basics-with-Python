product = input()
city = input()
quantity = float(input())
coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0
cost = 0

if city == "Sofia":
    if product == "coffee":
       coffee += 0.5 * quantity
       cost = coffee
    elif product == "water":
        water += 0.8 * quantity
        cost = water
    elif product == "beer":
        beer += 1.20 * quantity
        cost = beer
    elif product == "sweets":
        sweets += 1.45 * quantity
        cost = sweets
    elif product == "peanuts":
        peanuts += 1.60 * quantity
        cost = peanuts

if city == "Plovdiv":
    if product == "coffee":
       coffee += 0.4 * quantity
       cost = coffee
    elif product == "water":
        water += 0.7 * quantity
        cost = water
    elif product == "beer":
        beer += 1.15 * quantity
        cost = beer
    elif product == "sweets":
        sweets += 1.30 * quantity
        cost = sweets
    elif product == "peanuts":
        peanuts += 1.50 * quantity
        cost = peanuts

if city == "Varna":
    if product == "coffee":
       coffee += 0.45 * quantity
       cost = coffee
    elif product == "water":
        water += 0.7 * quantity
        cost = water
    elif product == "beer":
        beer += 1.10 * quantity
        cost = beer
    elif product == "sweets":
        sweets += 1.35 * quantity
        cost = sweets
    elif product == "peanuts":
        peanuts += 1.55 * quantity
        cost = peanuts

print(cost)
