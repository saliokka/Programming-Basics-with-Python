money_needed = float(input())
money_in_hand = float(input())
days_passed = 0
spent_days_row = 0
spent_too_much = False

while money_in_hand < money_needed:
    action = input()
    money = float(input())
    days_passed += 1

    if action == 'spend':
        spent_days_row += 1
        if spent_days_row == 5:
            spent_too_much = True
            break
        money_in_hand -= money
        if money_in_hand <= 0:
            money_in_hand = 0

    elif action == 'save':
        money_in_hand += money
        spent_days_row = 0
        if money_in_hand >= money_needed:
            break

if spent_too_much:
    print("You can't save the money.")
    print(days_passed)

else:
    print(f"You saved the money for {days_passed} days.")
