text = input()

rep = 1
for i in text:
    print(i * rep)
    rep += 1


i = 0
while (i < len(text)):
    print(text[i] * (i + 1))
    i += 1