h = int(input())
m = int(input())
m += 15
h += m//60
m %= 60
if h >= 24:
    h = 0
print(f"{h}:{m:02d}")
