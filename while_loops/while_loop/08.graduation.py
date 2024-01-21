name = input()
years_counter = 0
failed_years_counter = 0
grades_sum = 0

while True:

    yearly_grade = float(input())

    if yearly_grade < 4:
        failed_years_counter += 1
        if failed_years_counter == 2:
            print(f"{name} has been excluded at {years_counter +1 } grade")
            break
        continue

    years_counter += 1
    grades_sum += yearly_grade

    if years_counter == 12:
        avg_grade = grades_sum / years_counter
        print(f"{name} graduated. Average grade: {avg_grade:.02f}")
        break
