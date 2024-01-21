type_of_projection = input()
rows = int(input())
columns = int(input())
projection_cost = 0

if type_of_projection == "Premiere":
    projection_cost += 12.00
elif type_of_projection == "Normal":
    projection_cost += 7.50
elif type_of_projection == "Discount":
    projection_cost += 5.00
print(f"{projection_cost*rows*columns:.02f} leva")
