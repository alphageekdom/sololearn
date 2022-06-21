import re

password = input()

pattern = r"[A-Z]+[a-z]+[0-9]+"

if re.match(pattern, password):
    print("Password created")
else:
    print("Wrong format")