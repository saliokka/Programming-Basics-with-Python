meters = float(input())
price_per_meter = 7.61

total_sum = meters * price_per_meter

discount = total_sum * 0.18

print(f'The final price is: {total_sum - discount} lv.')
print(f'The discount price is: {discount} lv.')
