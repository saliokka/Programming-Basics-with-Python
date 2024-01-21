name = input()
points_from_the_academy = float(input())
judges_count = int(input())
total_points = 0
total_points += points_from_the_academy
goal = 1250.50

for i in range(judges_count):
    name_of_the_judge = input()
    points_from_the_judge = float(input())

    points_from_name = (len(name_of_the_judge) * points_from_the_judge) / 2
    total_points += points_from_name

if total_points > goal:
    print(f'Congratulations, {name} got a nominee for leading role with {total_points}!')

else:
    diff = abs(goal - total_points)
    print(f'Sorry, {name} you need {diff} more!')
