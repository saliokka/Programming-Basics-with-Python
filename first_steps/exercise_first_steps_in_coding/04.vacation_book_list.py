pages = int(input())
pages_per_h = int(input())
days = int(input())

hours_total = pages / pages_per_h

total_sum = hours_total / days

print(int(total_sum))
