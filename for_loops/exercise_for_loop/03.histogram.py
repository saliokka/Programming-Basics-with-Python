p1_counts = 0
p2_counts = 0
p3_counts = 0
p4_counts = 0
p5_counts = 0

reps = int(input())

for _ in range(reps):
    current_p_value = int(input())

    if current_p_value < 200:
        p1_counts += 1
    elif current_p_value < 400:
        p2_counts += 1
    elif current_p_value < 600:
        p3_counts += 1
    elif current_p_value < 800:
        p4_counts += 1
    else:
        p5_counts += 1

p1_percentage = p1_counts / reps * 100
p2_percentage = p2_counts / reps * 100
p3_percentage = p3_counts / reps * 100
p4_percentage = p4_counts / reps * 100
p5_percentage = p5_counts / reps * 100

print(f"{p1_percentage:.02f}%")
print(f"{p2_percentage:.02f}%")
print(f"{p3_percentage:.02f}%")
print(f"{p4_percentage:.02f}%")
print(f"{p5_percentage:.02f}%")
