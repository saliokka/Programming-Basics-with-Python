length_of_cake = int(input())
height_of_cake = int(input())

total_size = length_of_cake * height_of_cake

while total_size > 0:
    text = input()

    if text == 'STOP':
        break

    share = int(text)
    total_size -= share

if total_size > 0:
    print(f"{total_size} pieces are left.")
else:
    diff = abs(total_size)
    print(f'No more cake left! You need {diff} pieces more.')
