suma = float(input())
srok_na_deposita = float(input())
god_lih_pr = float(input())
natr_lih = suma * god_lih_pr/100
lih_za_1mes = natr_lih/12
obsh_sum = suma + srok_na_deposita * lih_za_1mes
print(obsh_sum)
