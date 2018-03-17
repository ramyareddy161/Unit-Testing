import unittest
from problem1 import get_right_rotations

class TestStringRotation(unittest.TestCase):
    score = 0
    def tearDown(self):
        print('Running Total: ', TestStringRotation.score)

    def test_get_right_rotations_method_1(self):
        self.assertEqual(get_right_rotations())
        TestStringRotation.score += 2
    
    def test_get_right_rotations_method_2(self):
        self.assertEqual(get_right_rotations())
        TestStringRotation.score += 3

    def test_get_right_rotations_method_3(self):
        self.assertEqual(get_right_rotations())
        TestStringRotation.score += 5

    def test_get_right_rotations_method_4(self):
        self.assertEqual(get_right_rotations())
        TestStringRotation.score += 5


if __name__ == '__main__':
    unittest.main()