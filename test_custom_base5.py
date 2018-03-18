import unittest
from problem2 import *

class TestCustomBase5(unittest.TestCase):
    score = 0
    def tearDown(self):
        print('Running Total: ', TestCustomBase5.score)

    def test_tocustombase5_method_1(self):
        self.assertEqual(to_custom_base5(0), 'a')
        TestCustomBase5.score += 2
    
    def test_tocustombase5_method_2(self):
        self.assertEqual(to_custom_base5(1001), 'bdaab')
        TestCustomBase5.score += 5

    def test_tocustombase5_method_3(self):
        self.assertEqual(to_custom_base5(-1001), '-bdaab')
        TestCustomBase5.score += 5

    def test_tocustombase5_method_4(self):
        with self.assertRaises(TypeError):
            result = to_custom_base5(3.2)
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        self.assertEqual(from_custom_base5(' bdeab '), 1101)
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        self.assertEqual(from_custom_base5(' -bdeab '), -1101)
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        self.assertEqual(from_custom_base5(' +bdeab '), 1101)
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        self.assertEqual(from_custom_base5('BDeab'), 1101)
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        with self.assertRaises(ValueError):
            result = from_custom_base5('BDhello')
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        with self.assertRaises(ValueError):
            result = from_custom_base5('bde-ab')
        TestCustomBase5.score += 3

    def test_fromcustombase5_method_4(self):
        with self.assertRaises(TypeError):
            result = from_custom_base5(10)
        TestCustomBase5.score += 2

if __name__ == '__main__':
    unittest.main()