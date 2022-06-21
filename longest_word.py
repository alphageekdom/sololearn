txt = input()

words = txt.split()

max_length = max(words, key=len)
print(max_length)