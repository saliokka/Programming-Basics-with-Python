n1 = int(input())
n2 = int(input())
operator = input()
eo = " "
sum = 0

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        sum += n1 + n2
    elif operator == "-":
        sum += n1 - n2
    elif operator == "*":
        sum += n1 * n2

    if sum % 2 == 0:
        eo = "even"
    else:
        eo = "odd"

    print(f"{n1} {operator} {n2} = {sum} - {eo}")

elif operator == "/" or operator == "%":
    if operator == "/":
        if n2 == 0:
            print(f"Cannot divide {n1} by zero")
            exit()
        sum += n1 / n2
        print(f"{n1} {operator} {n2} = {sum:.02f}")
    elif operator == "%":
        if n2 == 0:
            print(f"Cannot divide {n1} by zero")
            exit()
        sum += n1 % n2
        print(f"{n1} {operator} {n2} = {sum}")
