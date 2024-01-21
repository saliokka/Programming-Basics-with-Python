prc = float(input())
pq = int(input())
kq = int(input())
mq = int(input())
minq = int(input())
kamq = int(input())

totalq = pq+kq+mq+minq+kamq

profit = pq*2.6+kq*3+mq*4.1+minq*8.2+kamq*2

if totalq>=50:
    profit*=0.75

profit_plus_tax = profit*0.90
diff = abs(profit_plus_tax-prc)
if profit_plus_tax>=prc:
    print(f"Yes! {diff:.02f} lv left.")
else:
    print(f"Not enough money! {diff:.02f} lv needed.")
