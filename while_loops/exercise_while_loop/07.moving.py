width = int(input())
length = int(input())
height = int(input())
total_area = width * length * height
command = input()
space_none = False

while command != "Done":

    boxes = int(command)
    total_area -= boxes

    if total_area <= 0:
        space_none = True
        break
    command = input()

if space_none:
    print(f"No more free space! You need {abs(total_area)} Cubic meters more.")

else:
    print(f"{total_area} Cubic meters left.")
