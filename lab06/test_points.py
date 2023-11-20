import unittest
from points import Point

class TestPoint(unittest.TestCase):

    def test_str(self):
        point = Point(1, 2)
        self.assertEqual(str(point), "(1, 2)")

    def test_repr(self):
        point = Point(3, 4)
        self.assertEqual(repr(point), "Point(3, 4)")

    def test_eq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(3, 4))

    def test_ne(self):
        self.assertTrue(Point(1, 2) != Point(3, 4))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(5, 4) - Point(1, 2), Point(4, 2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)  # 1*4 - 2*3

    def test_length(self):
        self.assertEqual(Point(2, 3).length(), 3.605551275463989)

if __name__ == '__main__':
    unittest.main()
