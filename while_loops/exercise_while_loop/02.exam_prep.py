failed_problems_limit = int(input())
name_of_problem = input()
grade_counter = 0
total_problems = 0
total_failed_problems = 0
last_problem = ""
has_failed = False

while name_of_problem != "Enough":
    grade = int(input())
    total_problems += 1
    grade_counter += grade

    if grade <= 4:
        total_failed_problems += 1
        if total_failed_problems == failed_problems_limit:
            has_failed = True
            break
    last_problem = name_of_problem

    name_of_problem = input()

if has_failed:
    print(f"You need a break, {failed_problems_limit} poor grades.")

else:
    avg_score = grade_counter / total_problems

    print(f'Average score: {avg_score:.02f}')
    print(f'Number of problems: {total_problems}')
    print(f'Last problem: {last_problem}')
