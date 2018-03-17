import unittest
from problem16 import *

class TestTopEarners(unittest.TestCase):
    score = 0
    def tearDown(self):
        print('Running Total: ', TestTopEarners.score)

    def test_topearners_method_1(self):
        self.assertEqual(top_earners())
        TestTopEarners.score += 2
    
    def test_topearners_method_2(self):
        self.assertEqual(top_earners())
        TestTopEarners.score += 3

    def test_topearners_method_3(self):
        self.assertEqual(top_earners())
        TestTopEarners.score += 5

    def test_topearners_method_4(self):
        self.assertEqual(top_earners())
        TestTopEarners.score += 5

if __name__ == '__main__':
    unittest.main()