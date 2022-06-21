data = [
    [23, 11, 5, 14],
    [8, 32, 20, 5]
]

color = input()
eyes = ['brown','blue','green','black']
total = sum(data[0]) + sum(data[1])

for i in range(len(eyes)):
    if color == eyes[i]:
        x = data[0][i] + data[1][i]
        y = int((x/total) * 100)
        print(y)