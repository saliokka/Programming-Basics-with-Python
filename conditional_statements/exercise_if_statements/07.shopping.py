budget = float(input())
gpu_quantity = int(input())
cpu_quantity = int(input())
memory_quantity = int(input())

gpu_price = 250
total_gpu_sum = gpu_price*gpu_quantity
cpu_price = total_gpu_sum*0.35
memory_price = total_gpu_sum*0.10

total_cost = total_gpu_sum+cpu_quantity*cpu_price+memory_quantity*memory_price

if gpu_quantity > cpu_quantity:
    total_cost *= 0.85

diff = abs(budget-total_cost)

if budget >= total_cost:
    print(f"You have {diff:.02f} leva left!")
else:
    print(f"Not enough money! You need {diff:.02f} leva more!")
