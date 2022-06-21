import re

text = input()

pattern = r"#\w+"

match = re.findall(pattern, text)
for i in match:
    print(i)