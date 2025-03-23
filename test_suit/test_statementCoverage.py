import unittest
from isTriangle import Triangle
# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class TriangleTest(unittest.TestCase):
    def test1(self):
        '''checks if valid equilateral triangle returns EQUILATERAL type'''
        actual = Triangle.classify(10, 10, 10)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test2(self):
        '''checks if valid isosceles triangle returns ISOSCELES type'''
        abEqual = Triangle.classify(10, 10, 5) # side lengths a and b are equal, while side length c is less than a and b
        acEqual = Triangle.classify(10, 5, 10) # side lengths a and c are equal, while side length b is less than a and c
        bcEqual = Triangle.classify(5, 10, 10) # side lengths b and c are equal, while side length a is less than b and c
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(abEqual, expected)
        self.assertEqual(acEqual, expected)
        self.assertEqual(bcEqual, expected)
    
    def test3(self):
        '''checks if triangle with a non-positive side length returns INVALID type'''
        aZero = Triangle.classify(0, 10, 10) # side length a is zero
        bZero = Triangle.classify(10, 0, 10) # side length b is zero
        cZero = Triangle.classify(10, 10, 0) # side length c is zero
        expected = Triangle.Type.INVALID
        self.assertEqual(aZero, expected)
        self.assertEqual(bZero, expected)
        self.assertEqual(cZero, expected)

    def test4(self):
        '''checks if valid scalene triangle returns SCALENE type'''
        actual = Triangle.classify(4, 3, 2)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)
    
    def test5(self):
        '''checks if invalid scalene triangle returns INVALID type'''
        actual = Triangle.classify(2, 3, 1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
    
    def test6(self):
        '''checks if invalid isosceles triangle returns INVALID type'''
        abEqual = Triangle.classify(5, 5, 10) # side lengths a and b are equal, while side length c is greater than a and b
        acEqual = Triangle.classify(5, 10, 5) # side lengths a and c are equal, while side length b is greater than a and c
        bcEqual = Triangle.classify(10, 5, 5) # side lengths b and c are equal, while side length a is greater than b and c
        expected = Triangle.Type.INVALID
        self.assertEqual(abEqual, expected)
        self.assertEqual(acEqual, expected)
        self.assertEqual(bcEqual, expected)

if __name__ == '__main__':
    unittest.main()
