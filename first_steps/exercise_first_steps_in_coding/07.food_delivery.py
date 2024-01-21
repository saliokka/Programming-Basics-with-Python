chicken_menu_count = int(input())
fish_menu_count = int(input())
veg_menu_count = int(input())

chicken_menu_cost = float(10.35)
fish_menu_cost = float(12.40)
veg_menu_cost = float(8.15)

sum = chicken_menu_count*chicken_menu_cost + fish_menu_count * fish_menu_cost\
+ veg_menu_count*veg_menu_cost

dessert = (chicken_menu_count*chicken_menu_cost + fish_menu_count * fish_menu_cost\
+ veg_menu_count*veg_menu_cost) * 0.2

final_sum = sum + dessert + 2.5
print(final_sum)
