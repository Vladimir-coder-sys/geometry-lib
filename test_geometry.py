import unittest
from geometry import Circle, Triangle


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.area(), 3.14159, places=4)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=4)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_non_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_triangle())


if __name__ == "__main__":
    unittest.main()
