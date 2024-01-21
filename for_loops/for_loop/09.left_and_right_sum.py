first_sum = 0
second_sum = 0

reps = int(input())

for _ in range(reps):
    first_sum_number = int(input())
    first_sum += first_sum_number
for _ in range(reps):
    second_sum_number = int(input())
    second_sum += second_sum_number

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")

elif first_sum != second_sum:
    print(f"No, diff = {abs(second_sum-first_sum)}")
