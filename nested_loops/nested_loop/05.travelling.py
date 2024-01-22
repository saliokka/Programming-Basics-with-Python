destination = input()
total_savings = 0

while destination != "End":
    minimal_cash_for_the_trip = float(input())

    while minimal_cash_for_the_trip > total_savings:
        current_saving = float(input())
        total_savings += current_saving
    print(f"Going to {destination}!")
    total_savings = 0
    destination = input()
