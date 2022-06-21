from data import data

age = int(input())

data_values = data.values()

current = 0
new = 0

for x in data_values:
    if x >= 18:
        current += 20
    else:
        current += 5

for x in data_values:
    if x >= age:
        new += 20
    else:
        new += 5


res = ((new - current)/ current) * 100

print(int(res))