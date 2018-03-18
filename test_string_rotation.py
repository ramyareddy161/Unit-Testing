import unittest
from problem1 import get_right_rotations

class TestStringRotation(unittest.TestCase):
    score = 0
    def tearDown(self):
        print('Running Total: ', TestStringRotation.score)

    def test_get_right_rotations_method_1(self):
        self.assertEqual(get_right_rotations(None, None), -1)
        TestStringRotation.score += 1
    
    def test_get_right_rotations_method_2(self):
        self.assertEqual(get_right_rotations(None, 'abcd'), -1)
        TestStringRotation.score += 1

    def test_get_right_rotations_method_3(self):
        self.assertEqual(get_right_rotations('abcd', 'acbd'), -1)
        TestStringRotation.score += 4

    def test_get_right_rotations_method_4(self):
        self.assertEqual(get_right_rotations('abcd', 'cdab'), 2)
        TestStringRotation.score += 5
    
    def test_get_right_rotations_method_5(self):
        self.assertEqual(get_right_rotations('aeiou', 'aeiou'), 0)
        TestStringRotation.score += 4

if __name__ == '__main__':
    unittest.main()