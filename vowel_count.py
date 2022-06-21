text = input().lower()
res = [letter for letter in text if letter in "aeiou"]
print(len(res))