text = input()

x = len(text.split())
y = len(text.replace(' ',''))
print(float(y/x))