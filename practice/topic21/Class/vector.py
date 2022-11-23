class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Vector(abs(self.x), abs(self.y))

    def __round__(self, n=None):
        return Vector(round(self.x, n), round(self.y, n))

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return Vector(self.x // other, self.y // other)

    def __mod__(self, other):
        return Vector(self.x % other, self.y % other)

    def __iter__(self):
        return self.intpair().__iter__()

    # task3
    def intpair(self):
        a = int(round(self.x))
        b = int(round(self.y))
        return (a, b)


# Используя класс Vector выведите координаты центра масс данного множества точек.
def center_mass(list_point: list):
    vector_list = [Vector(a, b) for a, b in list_point]
    res = Vector()
    for v in vector_list:
        res += v
    return res / len(list_point)

#DONE!
