from math import floor
number_of_competitions = int(input())
starting_points = int(input())
total_points = starting_points
tournaments_won = 0
for _ in range(number_of_competitions):
    result = input()
    if result == "W":
        total_points += 2000
        tournaments_won += 1
    elif result == "F":
        total_points += 1200
    elif result == "SF":
        total_points += 720

average_points_earned = (total_points - starting_points) / number_of_competitions
win_rate = tournaments_won / number_of_competitions * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points_earned)}")
print(f"{win_rate:.02f}%")
