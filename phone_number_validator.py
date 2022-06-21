import re

text = input()

pattern = r"^[189][0-9]{7}"

match = re.match(pattern, text)
if match:
    print("Valid")
else:
    print("Invalid")