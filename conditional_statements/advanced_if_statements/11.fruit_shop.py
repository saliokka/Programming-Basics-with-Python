food_type = input()
day_of_week = input()
quantity = float(input())
price_of_food = 0


if day_of_week == "Monday" or day_of_week == "Tuesday" or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" or day_of_week == "Friday":

    if food_type == "banana":
        price_of_food += 2.50

    elif food_type == "apple":
        price_of_food += 1.20

    elif food_type == "orange":
        price_of_food += 0.85

    elif food_type == "grapefruit":
        price_of_food += 1.45

    elif food_type == "kiwi":
        price_of_food += 2.70

    elif food_type == "pineapple":
        price_of_food += 5.50

    elif food_type == "grapes":
        price_of_food += 3.85

elif day_of_week == "Saturday" or day_of_week == "Sunday":

    if food_type == "banana":
        price_of_food += 2.70

    elif food_type == "apple":
        price_of_food += 1.25

    elif food_type == "orange":
        price_of_food += 0.90

    elif food_type == "grapefruit":
        price_of_food += 1.60

    elif food_type == "kiwi":
        price_of_food += 3.00

    elif food_type == "pineapple":
        price_of_food += 5.60

    elif food_type == "grapes":
        price_of_food += 4.20

cost = price_of_food * quantity

if cost == 0.00:
    print("error")
else:
    print(f"{cost:.02f}")
