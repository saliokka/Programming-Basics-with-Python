nylon_q = int(input())
paint_q = int(input())
razreditel_q = int(input())
work_hours = int(input())
nylon_price = 1.5
paint_price = 14.50
razreditel_price = 5.00
bags = 0.4

price_for_materials = (nylon_q+2) * nylon_price + paint_q * (paint_price*1.1) + razreditel_q * razreditel_price + bags

worker_payment = (price_for_materials * 0.3) * work_hours

final_sum = price_for_materials + worker_payment
print(final_sum)
