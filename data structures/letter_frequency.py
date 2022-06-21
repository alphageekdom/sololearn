text = input()
letter = input()

x = len(text)
y = text.count(letter)

print(int(y/x * 100))