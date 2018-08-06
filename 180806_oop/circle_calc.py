import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pow(self.radius, 2) * math.pi

    def __str__(self):
        return "radius: " + str(self.radius)


c1 = Circle(10)
c2 = Circle(5)

print(c1.getArea())
print(c2.getArea())