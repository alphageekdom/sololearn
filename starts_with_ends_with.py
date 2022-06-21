import re

word = input()
pattern = r"^m..e"

if re.match(pattern, word):
    print("Match")
else:
    print("No match")