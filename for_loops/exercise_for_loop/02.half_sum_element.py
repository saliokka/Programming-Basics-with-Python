from sys import maxsize

total_sum = 0
max_number = -maxsize

reps = int(input())

for _ in range(reps):
    current_number = int(input())
    total_sum += current_number
    if max_number < current_number:
        max_number = current_number

if total_sum - max_number == max_number:
    print(f"Yes")
    print(f"Sum = {max_number}")
else:
    total_sum = total_sum - max_number
    print(f"No")
    print(f"Diff = {abs(max_number-total_sum)}")
