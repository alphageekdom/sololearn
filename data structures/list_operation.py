data = [
    [23, 11, 5, 14],
    [8, 32, 20, 5],
]

color = input()
total = sum(data[0] + data[1])
eyes = ["brown", "blue", "green", "black"]

if color == "brown":
    print(int((data[0][0] + data[1][0]) / total * 100))
elif color == "blue":
    print(int((data[0][1] + data[1][1]) / total * 100))
elif color == "green":
    print(int((data[0][2] + data[1][2]) / total * 100))
elif color == "black":
    print(int((data[0][3] + data[1][3]) / total * 100))