length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
obstacles_percent = float(input())

obem = length_cm * width_cm * height_cm
obem_in_liters = obem * 0.001
obstacles_percent = obstacles_percent / 100
req_liters = obem_in_liters * (1 - obstacles_percent)
print(req_liters)
