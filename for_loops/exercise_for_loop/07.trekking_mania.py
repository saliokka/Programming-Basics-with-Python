total_group_of_climbers = int(input())

musala_climbers_group = 0
monblan_climbers_group = 0
kilimanjaro_climbers_group = 0
k2_climbers_group = 0
everest_climbers_group = 0
total_climbers = 0
for _ in range(total_group_of_climbers):
    people_in_a_group = int(input())
    total_climbers += people_in_a_group
    if people_in_a_group < 6:
        musala_climbers_group += people_in_a_group

    elif people_in_a_group < 13:
        monblan_climbers_group += people_in_a_group

    elif people_in_a_group < 26:
        kilimanjaro_climbers_group += people_in_a_group

    elif people_in_a_group < 41:
        k2_climbers_group += people_in_a_group

    else:
        everest_climbers_group += people_in_a_group

percentage_musala_climbers = musala_climbers_group / total_climbers * 100
percentage_kilimanjaro_climbers = kilimanjaro_climbers_group / total_climbers * 100
percentage_monblan_climbers = monblan_climbers_group / total_climbers * 100
percentage_k2_climbers = k2_climbers_group / total_climbers * 100
percentage_everest_climbers = everest_climbers_group / total_climbers * 100

print(f"{percentage_musala_climbers:.02f}%")
print(f"{percentage_monblan_climbers:.02f}%")
print(f"{percentage_kilimanjaro_climbers:.02f}%")
print(f"{percentage_k2_climbers:.02f}%")
print(f"{percentage_everest_climbers:.02f}%")
