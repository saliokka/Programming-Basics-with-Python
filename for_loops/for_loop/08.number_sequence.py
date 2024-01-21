from sys import maxsize

reps = int(input())
max_number = -maxsize
min_number = maxsize

for _ in range(reps):
    current_number = int(input())
    if max_number < current_number:
        max_number = current_number
    if min_number > current_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
