fi = int(input())
se = int(input())
th = int(input())
tt = fi+se+th
mins = tt//60
secs = tt % 60
if secs<10:
    print(f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")
