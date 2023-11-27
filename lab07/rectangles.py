from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Podano nieprawidlowe wspolrzedne: x1<x2, y1<y2")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other): # obsluga rect1 == rect2
        if not isinstance(other, Rectangle):
            return False # NotImplemented
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other): # obsluga rect1 != rect2
        return not self == other

    def center(self): # zwraca srodek prostokąta
        centerX = (self.pt1.x + self.pt2.x) / 2
        centerY = (self.pt1.y + self.pt2.y) / 2
        return Point(centerX, centerY)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y): # przesuniecie o (x, y)
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Argumenty x i y musza byc liczbami")
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self

    def intersection(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Argument nie jest instancja Rectangle")

        # Wspolrzedne czesci wspolnej
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        # Warunek jak przy init
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2, y2)
        return None

    def cover(self, other):
        if not isinstance(other, Rectangle):
            raise ValueError("Argument nie jest instancja Rectangle")

        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        # Obliczenie srodka
        centerX = (self.pt1.x + self.pt2.x) / 2
        centerY = (self.pt1.y + self.pt2.y) / 2

        # 4 mniejsze prostokaty
        r1 = Rectangle(self.pt1.x, self.pt1.y, centerX, centerY) # lewy dolny
        r2 = Rectangle(centerX, self.pt1.y, self.pt2.x, centerY) # prawy dolny
        r3 = Rectangle(self.pt1.x, centerY, centerX, self.pt2.y) # lewy gorny
        r4 = Rectangle(centerX, centerY, self.pt2.x, self.pt2.y) # prawy gorny

        return (r1, r2, r3, r4)
