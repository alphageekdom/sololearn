text = input()
letter = input()

x = len(text)
y = text.count(letter)

f = int((y/x) * 100)
print(f)