import unittest
import main as calc
from math import ceil

class TestCalculator(unittest.TestCase):
    def test_triangle_no_compile_time(self):
        self.assertEqual(calc.getArea(3, 4, 5), 6)
    
    def test_circle_no_compile_time(self):
        self.assertEqual(ceil(calc.getArea(5)), 79)
    
    def test_triangle_is_rectangle_no_compile_time(self):
        self.assertEqual(calc.getArea(3, 3, 0), 4.5)

    def test_two_arguments(self):
        with self.assertRaises(ValueError):
            calc.getArea(3, 4)

if __name__ == '__main__':
    unittest.main()

