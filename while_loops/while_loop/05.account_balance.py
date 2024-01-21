total_sum = 0

while True:
    text = input()
    if text == "NoMoreMoney":
        break

    current_deposit = float(text)

    if current_deposit < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {current_deposit:.02f}")
    total_sum += current_deposit

print(f"Total: {total_sum:.02f}")
