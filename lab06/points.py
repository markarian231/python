class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstruktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self): # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other): # obsluga point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other): # obsluga point1 != point2
        return not self == other # uzycie operatora __eq__

    def __add__(self, other): # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other): # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other): # v1 * v2, iloczyn skalarny, zwraca liczbe
        return self.x * other.x + self.y * other.y

    def cross(self, other): # v1 x v2, iloczyn wektorowy 2D, zwraca liczbe
        return self.x * other.y - self.y * other.x

    def length(self): # długosc wektora (** - potega)
        return (self.x**2 + self.y**2)**0.5

    def __hash__(self):
        return hash((self.x, self.y))
