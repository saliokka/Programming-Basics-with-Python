number = int(input())
counter = 1
has_exceeded = False
for rows in range(1, number + 1):
    for columns in range(1, rows + 1):
        print(counter, end = ' ')
        counter += 1
        if counter > number:
            has_exceeded = True
            break
    if has_exceeded:
        break
    print()
