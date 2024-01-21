day_of_week = input()
cost_of_ticket = 0

if day_of_week == 'Monday' or day_of_week == 'Friday' or day_of_week == 'Tuesday':
    cost_of_ticket += 12

elif day_of_week == 'Wednesday' or day_of_week == 'Thursday':
    cost_of_ticket += 14


elif day_of_week == "Sunday" or day_of_week == "Saturday":
    cost_of_ticket += 16

print(cost_of_ticket)
