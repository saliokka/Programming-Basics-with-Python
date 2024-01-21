txt = input()
khotun = 0
for letter in txt:
    if letter == "a":
        khotun += 1
    elif letter == "e":
        khotun += 2
    elif letter == "i":
        khotun += 3
    elif letter == "o":
        khotun += 4
    elif letter == "u":
        khotun += 5

print(khotun)
