import string

def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = "new_file.txt"
with open(filename) as f:
    text = f.read()
    print(text)

for char in string.ascii_lowercase:
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))