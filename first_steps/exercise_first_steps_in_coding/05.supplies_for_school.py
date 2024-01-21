himikal_broika = int(input())
marker_broika = int(input())
preparat_broika = int(input())
procent_namalenie = int(input())



himikal_cena = 5.8
marker_cena = 7.2
preparat_cena = 1.2
discount= procent_namalenie/100

obshta_cena = (himikal_broika*himikal_cena+marker_broika*marker_cena+preparat_broika*preparat_cena)
obshta_cena = obshta_cena-(obshta_cena*discount)
print(obshta_cena)
