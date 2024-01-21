money_collected = 0
toy_quantity = 0
birthday_money = 0

lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

for each_year in range(1, lily_age+1):
    if each_year % 2 == 0:
        birthday_money += 10
        money_collected += birthday_money - 1
    elif each_year % 2 != 0:
        toy_quantity += 1

money_collected += toy_quantity * toy_price

if money_collected >= washing_machine_price:
    print(f"Yes! {money_collected - washing_machine_price:.02f}")
else:
    print(f"No! {abs(washing_machine_price-money_collected):.02f}")
