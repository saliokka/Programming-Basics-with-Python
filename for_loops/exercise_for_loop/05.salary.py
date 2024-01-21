tabs = int(input())
salary = int(input())

for _ in range(tabs):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == "Instagram":
        salary -= 100
    elif tab_name == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
