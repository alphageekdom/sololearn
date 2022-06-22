contacts = {
    ("James", 42),
    ("Amy", 24),
    ("John", 31),
    ("Amanda", 63),
    ("Bob", 18),
}

name = input()

for x in contacts:
    if name in x:
        print(f"{x[0]} is {x[1]}")
        break
else:
    print("Not Found")