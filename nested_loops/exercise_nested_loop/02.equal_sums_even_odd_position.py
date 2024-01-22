number1 = int(input())
number2 = int(input())

for current_number in range(number1, number2 + 1):
    odd_positions_sum = 0
    even_positions_sum = 0
    current_number_in_string = str(current_number)
    for index, digit in enumerate(current_number_in_string):

        if index % 2 == 0:
            odd_positions_sum += int(digit)
        else:
            even_positions_sum += int(digit)

    if odd_positions_sum == even_positions_sum:
        print(current_number, end=" ")
