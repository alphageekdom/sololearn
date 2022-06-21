import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

text = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, text)
if match:
    print(match.group())