import unittest
from rectangles import Rectangle
from points import Point

class TestRectangle(unittest.TestCase):

    def test_str(self):
        rect = Rectangle(0, 0, 1, 1)
        self.assertEqual(str(rect), "[(0, 0), (1, 1)]")

    def test_repr(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(repr(rect), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertTrue(Rectangle(0, 0, 1, 1) == Rectangle(0, 0, 1, 1))
        self.assertFalse(Rectangle(0, 0, 1, 1) == Rectangle(1, 1, 2, 2))

    def test_ne(self):
        self.assertTrue(Rectangle(0, 0, 1, 1) != Rectangle(1, 1, 2, 2))
        self.assertFalse(Rectangle(0, 0, 1, 1) != Rectangle(0, 0, 1, 1))

    def test_center(self):
        rect = Rectangle(0, 0, 2, 2)
        self.assertEqual(rect.center(), Point(1, 1))

    def test_area(self):
        rect = Rectangle(0, 0, 1, 1)
        self.assertEqual(rect.area(), 1)

    def test_move(self):
        rect = Rectangle(0, 0, 1, 1)
        moved_rect = rect.move(1, 1)
        self.assertEqual(moved_rect, Rectangle(1, 1, 2, 2))

    def test_intersection(self):
        rect1 = Rectangle(0, 0, 2, 2)
        rect2 = Rectangle(1, 1, 3, 3)
        self.assertEqual(rect1.intersection(rect2), Rectangle(1, 1, 2, 2))

    def test_cover(self):
        rect1 = Rectangle(0, 0, 1, 1)
        rect2 = Rectangle(1, 1, 2, 2)
        self.assertEqual(rect1.cover(rect2), Rectangle(0, 0, 2, 2))

    def test_make4(self):
        rect = Rectangle(0, 0, 2, 2)
        r1, r2, r3, r4 = rect.make4()
        self.assertEqual(r1, Rectangle(0, 0, 1, 1))
        self.assertEqual(r2, Rectangle(1, 0, 2, 1))
        self.assertEqual(r3, Rectangle(0, 1, 1, 2))
        self.assertEqual(r4, Rectangle(1, 1, 2, 2))

if __name__ == '__main__':
    unittest.main()
