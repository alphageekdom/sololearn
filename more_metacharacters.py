import re

# pattern = r"egg(spam)*"

# if re.match(pattern, "egg"):
#     print("Match 1")

# if re.match(pattern, "eggspamspamegg"):
#     print("Match 2")

# if re.match(pattern, "spam"):
#     print("Match 3")

# pattern = r"g+"

# if re.match(pattern, "g"):
#     print("Match 1")

# if re.match(pattern, "gggggggggg"):
#     print("Match 2")

# if re.match(pattern, "abdcdef"):
#     print("Match 3")

# pattern = r"ice(-)?cream"

# if re.match(pattern, "ice-cream"):
#     print("Match 1")

# if re.match(pattern, "icecream"):
#     print("Match 2")

# if re.match(pattern, "sausages"):
#     print("Match 3")

# if re.match(pattern, "ice--ice"):
#     print("Match 4")

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")

if re.match(pattern, "999"):
    print("Match 2")

if re.match(pattern, "9999"):
    print("Match 3")