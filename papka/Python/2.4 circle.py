import math
shape = int(input("Choose:\n1.Triange\n2.Rectangle\n3.Circle\n"))
if shape == 1:
    base = int(input("Base of triange: "))
    height = int(input("Height of triange: "))
    print((height * base) / 2)
elif shape == 2:
    length = int(input("Length of rectangle: "))
    width = int(input("Width of rectangle: "))
    print(length * width)
else:
    radius = int(input("Radius of circle: "))
    print(math.pi * radius ** 2)
