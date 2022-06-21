points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90),
]

distance = []
for (x, y) in points:
    z = (x**2 + y**2)**0.5
    distance.append(z)


print(min(distance))