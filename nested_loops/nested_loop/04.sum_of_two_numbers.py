start = int(input())
finish = int(input())
magic_n = int(input())
has_finished = False
combo = 0

for x1 in range(start, finish + 1):
    for x2 in range(start, finish + 1):
        combo += 1
        if x1 + x2 == magic_n:
            has_finished = True
            print(f"Combination N:{combo} ({x1} + {x2} = {magic_n})")
            break
    if has_finished:
        break

if not has_finished:
    print(f"{combo} combinations - neither equals {magic_n}")
