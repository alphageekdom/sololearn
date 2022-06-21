text = """Amy has 128 dollars, while David has 54 dollars.
Amy is going to the zoo. David watches soccer."""

entry_1, entry_2 = input(), input()

x = text.count(entry_1)
y = text.replace(entry_1, entry_2)

print(x)
print(y)