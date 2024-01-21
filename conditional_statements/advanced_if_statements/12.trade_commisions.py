city = input()
obem_na_prodajbi = float(input())

if city == "Sofia":
    if 0 <= obem_na_prodajbi <= 500:
        obem_na_prodajbi *= 0.05
        print(f"{obem_na_prodajbi:.02f}")
    elif 500 <= obem_na_prodajbi <= 1000:
        obem_na_prodajbi *= 0.07
        print(f"{obem_na_prodajbi:.02f}")
    elif 1000 <= obem_na_prodajbi <= 10000:
        obem_na_prodajbi *= 0.08
        print(f"{obem_na_prodajbi:.02f}")
    elif obem_na_prodajbi > 10000:
        obem_na_prodajbi *= 0.12
        print(f"{obem_na_prodajbi:.02f}")
    else:
        print("error")

elif city == "Varna":
    if 0 <= obem_na_prodajbi <= 500:
        obem_na_prodajbi *= 0.045
        print(f"{obem_na_prodajbi:.02f}")
    elif 500 <= obem_na_prodajbi <= 1000:
        obem_na_prodajbi *= 0.075
        print(f"{obem_na_prodajbi:.02f}")
    elif 1000 <= obem_na_prodajbi <= 10000:
        obem_na_prodajbi *= 0.10
        print(f"{obem_na_prodajbi:.02f}")
    elif obem_na_prodajbi > 10000:
        obem_na_prodajbi *= 0.13
        print(f"{obem_na_prodajbi:.02f}")
    else:
        print("error")


elif city == "Plovdiv":
    if 0 <= obem_na_prodajbi <= 500:
        obem_na_prodajbi *= 0.055
        print(f"{obem_na_prodajbi:.02f}")
    elif 500 <= obem_na_prodajbi <= 1000:
        obem_na_prodajbi *= 0.08
        print(f"{obem_na_prodajbi:.02f}")
    elif 1000 <= obem_na_prodajbi <= 10000:
        obem_na_prodajbi *= 0.12
        print(f"{obem_na_prodajbi:.02f}")
    elif obem_na_prodajbi > 10000:
        obem_na_prodajbi *= 0.145
        print(f"{obem_na_prodajbi:.02f}")
    else:
        print("error")
else:
        print("error")
