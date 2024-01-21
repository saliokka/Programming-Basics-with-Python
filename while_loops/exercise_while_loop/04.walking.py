total_steps_sum = 0
goal = 10000

while total_steps_sum < goal:
    command = input()
    if command == "Going home":
        steps_while_going_home = int(input())
        total_steps_sum += steps_while_going_home
        break
    command = int(command)
    total_steps_sum += command

if total_steps_sum >= goal:
    diff = total_steps_sum - goal
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

else:
    diff = goal - total_steps_sum
    print(f'{diff} more steps to reach goal.')
