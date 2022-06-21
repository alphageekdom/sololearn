import math

p1 = (23, -88)
p2 = (6, 42)

horizontal = (p1[0] - p2[0])**2
vertical = (p1[1] - p2[1])**2
distance = math.sqrt(horizontal + vertical)
print(distance)