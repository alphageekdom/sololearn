points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

coord = []
for (x,y) in points:
    z = ((x**2) + (y**2))**(1/2)
    coord.append(z)
print(min(coord))